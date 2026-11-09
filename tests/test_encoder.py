"""Unit tests for zerorl.helpers.encoder.ObservationEncoder."""

import pytest
import torch
from torch import nn

from zerorl.helpers.encoder import ObservationEncoder


class TestVectorPaths:
    def test_int_and_tuple_shapes_equivalent(self) -> None:
        e_int = ObservationEncoder(8)
        e_tup = ObservationEncoder((8,))
        x = torch.randn(5, 8)
        assert e_int.output_dim == e_tup.output_dim == 8
        assert torch.equal(e_int(x), e_tup(x))
        # vector encoders are pure flattening: ZERO parameters, which is
        # what keeps the shared-trunk reference/sd contract intact
        assert sum(p.numel() for p in e_int.parameters()) == 0
        assert e_int.is_image is False and e_int.image_layout is None

    def test_multidim_vector_flattens(self) -> None:
        enc = ObservationEncoder((4, 5))
        assert enc.output_dim == 20
        out = enc(torch.randn(2, 4, 5))
        assert out.shape == (2, 20)

    def test_single_sample_gets_batched(self) -> None:
        enc = ObservationEncoder(8)
        assert enc(torch.randn(8)).shape == (1, 8)
        assert enc(torch.randn(3, 8)).shape == (3, 8)

    def test_invalid_shapes_and_scale_raise(self) -> None:
        with pytest.raises(ValueError, match="Invalid observation shape"):
            ObservationEncoder(0)
        with pytest.raises(ValueError, match="Invalid observation shape"):
            ObservationEncoder((-3,))
        with pytest.raises(ValueError, match="image_scale"):
            ObservationEncoder(8, image_scale=0)


class TestImagePaths:
    def test_hwc_and_chw_equivalent_after_layout(self) -> None:
        torch.manual_seed(0)
        chw = ObservationEncoder((3, 84, 84), image_layout="CHW")
        hwc = ObservationEncoder((84, 84, 3), image_layout="HWC")
        hwc.features.load_state_dict(chw.features.state_dict())
        img = torch.rand(2, 3, 84, 84) * 255.0
        out_chw = chw(img)
        out_hwc = hwc(img.permute(0, 2, 3, 1).contiguous())
        assert out_chw.shape == out_hwc.shape
        assert torch.allclose(out_chw, out_hwc, atol=1e-6)

    def test_auto_layout_detection(self) -> None:
        assert ObservationEncoder((3, 84, 84)).image_layout == "CHW"
        assert ObservationEncoder((84, 84, 3)).image_layout == "HWC"
        # ambiguous: both first and last look like channels
        with pytest.raises(ValueError, match="Cannot infer image layout"):
            ObservationEncoder((3, 8, 3))

    def test_bad_explicit_layout_raises(self) -> None:
        with pytest.raises(ValueError, match="image_layout"):
            ObservationEncoder((3, 84, 84), image_layout="XYZ")

    def test_pixel_scale_applied_only_when_enabled(self) -> None:
        class Recorder(nn.Module):
            def __init__(self) -> None:
                super().__init__()
                self.seen = None

            def forward(self, x):
                self.seen = x
                return x.flatten(1)

        enc = ObservationEncoder((3, 84, 84), image_scale=255.0)
        rec = Recorder()
        enc.features = rec
        enc(torch.full((1, 3, 84, 84), 255.0))
        assert rec.seen is not None and float(rec.seen.max()) == pytest.approx(1.0)

        enc_ns = ObservationEncoder((3, 84, 84), image_scale=None)
        rec2 = Recorder()
        enc_ns.features = rec2
        enc_ns(torch.full((1, 3, 84, 84), 255.0))
        assert float(rec2.seen.max()) == pytest.approx(255.0)

    def test_too_small_image_raises(self) -> None:
        with pytest.raises(ValueError, match="too small"):
            ObservationEncoder((1, 4, 4), image_layout="CHW")

    def test_output_dim_matches_forward(self) -> None:
        enc = ObservationEncoder((1, 84, 84))
        out = enc(torch.zeros(1, 1, 84, 84))
        assert enc.output_dim == out.shape[-1]
        assert enc.n_features == enc.output_dim

"""Unit tests for zerorl.helpers.sweeps (wandb/optuna wrappers)."""

import sys
import types

import pytest

from zerorl.helpers.sweeps import run_optuna_sweep, run_wandb_sweep


def test_wandb_missing_raises_install_hint(monkeypatch) -> None:
    monkeypatch.setitem(sys.modules, "wandb", None)
    with pytest.raises(ImportError, match="wandb"):
        run_wandb_sweep({"method": "grid"}, lambda: None, "proj")


def test_optuna_missing_raises_install_hint(monkeypatch) -> None:
    monkeypatch.setitem(sys.modules, "optuna", None)
    with pytest.raises(ImportError, match="optuna"):
        run_optuna_sweep(lambda trial: 0.0)


def test_wandb_delegates_to_sweep_and_agent(monkeypatch) -> None:
    calls = {}
    mod = types.ModuleType("wandb")

    def sweep(**kwargs):
        calls["sweep"] = kwargs
        return "sweep-id-1"

    def agent(sweep_id, function=None, count=None):
        calls["agent"] = (sweep_id, count, function)

    mod.sweep = sweep
    mod.agent = agent
    monkeypatch.setitem(sys.modules, "wandb", mod)

    fn = lambda: None  # noqa: E731
    run_wandb_sweep({"method": "grid"}, fn, "my-proj", num_trials=3)
    assert calls["sweep"] == {"sweep": {"method": "grid"}, "project": "my-proj"}
    assert calls["agent"] == ("sweep-id-1", 3, fn)


def test_optuna_delegates_to_create_study_and_optimize(monkeypatch) -> None:
    calls = {}
    mod = types.ModuleType("optuna")

    class _Study:
        best_params = {"lr": 0.01}

        # NOTE: class-attribute callables receive `self` as first arg —
        # declaring it is required or the bound self lands in `fn`.
        def optimize(self, fn, n_trials=None, **kwargs):
            calls["optimize"] = (fn, n_trials)

    def create_study(**kwargs):
        calls["create_study"] = kwargs
        return _Study()

    mod.create_study = create_study
    monkeypatch.setitem(sys.modules, "optuna", mod)

    def objective(trial):
        return 1.0

    best = run_optuna_sweep(objective, direction="minimize", num_trials=5)
    assert calls["create_study"] == {"direction": "minimize"}
    assert calls["optimize"] == (objective, 5)
    assert best == {"lr": 0.01}

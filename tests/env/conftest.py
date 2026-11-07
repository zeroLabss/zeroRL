"""Shared fixtures for env tests."""

import os
import subprocess
import sys
from functools import lru_cache

import pytest

# Minimal scene + the exact operation that has crashed CI natively:
# creating a mujoco.Renderer (EGL/OSMesa context). A native SIGABRT inside
# it would kill the whole pytest session, so the capability check runs in a
# SUBPROCESS where a crash/timeout can only fail the probe, not the suite.
_RENDER_PROBE = """
import mujoco
m = mujoco.MjModel.from_xml_string(
    "<mujoco><worldbody><body pos='0 0 0'/></worldbody></mujoco>"
)
mujoco.Renderer(m, 32, 32)
"""


@lru_cache(maxsize=1)
def mujoco_render_works() -> bool:
    """True only if a real MuJoCo renderer can be created here.

    Trusts nothing (env vars like MUJOCO_GL are inherited by the probe but
    are claims, not capabilities): the probe either exits 0, times out, or
    crashes — anything but 0 means rendering is unavailable on this host.
    """
    try:
        proc = subprocess.run(
            [sys.executable, "-c", _RENDER_PROBE],
            capture_output=True, text=True, timeout=30,
            env=dict(os.environ),
        )
        return proc.returncode == 0
    except Exception:
        return False


@pytest.fixture
def mujoco_gl() -> None:
    if not mujoco_render_works():
        pytest.skip(
            "MuJoCo renderer unavailable on this host "
            "(no usable GL/EGL context; probe failed or crashed)"
        )

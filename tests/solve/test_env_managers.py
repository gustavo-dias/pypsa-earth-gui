"""Tests for the module env_managers.py"""

from typing import Generator

from pytest_subprocess.fixtures import FakeProcess, fp

from app.solve.env_managers import EnvManager
from app.solve.env_managers import get_installed_python_env_managers


def test_env_managers() -> None:
    """"""
    assert EnvManager.to_list() == \
        [EnvManager.CONDA, EnvManager.MAMBA]


def test_get_installed_python_env_managers(
        fp: Generator[FakeProcess, None, None]
    ) -> None:
    """"""
     # 127: exit code for 'command not found' (unistalled); run $? to inspect
    fp.register([EnvManager.MAMBA, '--version'], returncode=127) #type: ignore
    fp.register([EnvManager.CONDA, '--version'], returncode=127) #type: ignore

    assert get_installed_python_env_managers(EnvManager.to_list()) == \
        [], "neither installed"

    fp.register([EnvManager.MAMBA, '--version'], returncode=0) #type: ignore
    fp.register([EnvManager.CONDA, '--version'], returncode=127) #type: ignore

    assert get_installed_python_env_managers(EnvManager.to_list()) == \
        [EnvManager.MAMBA], "mamba only insalled"

    fp.register([EnvManager.MAMBA, '--version'], returncode=0) #type: ignore
    fp.register([EnvManager.CONDA, '--version'], returncode=0) #type: ignore

    assert get_installed_python_env_managers(EnvManager.to_list()) == \
        EnvManager.to_list(), "mamba and conda installed"

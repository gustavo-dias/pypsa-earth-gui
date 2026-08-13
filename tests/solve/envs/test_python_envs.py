"""Tests for the module python_envs.py"""

from json import dumps
from typing import Generator
from pytest_subprocess.fixtures import FakeProcess, fp

from app.solve.env_managers import EnvManager
from app.solve.envs.python_envs import get_available_python_envs


def test_get_available_python_envs(
        fp: Generator[FakeProcess, None, None]
    ) -> None:
    """"""
    cmd = [EnvManager.CONDA, 'env', 'list', '--json']
    stdout = {
        'envs': [
            '/path/to/base',
            '/path/to/envs/env_1',
            '/path/to/envs/env_2',
        ]
    }
    fp.register(cmd, dumps(stdout), returncode=0) #type: ignore
    assert get_available_python_envs(EnvManager.CONDA) == \
        ['env_1', 'env_2'], 'success'

    fp.register(cmd, dumps(stdout), returncode=1) #type: ignore
    assert get_available_python_envs(EnvManager.CONDA) == None, 'error on run'

    stdout = {}
    fp.register(cmd, dumps(stdout), returncode=0) #type: ignore
    assert get_available_python_envs(EnvManager.CONDA) == [], 'no environments'

    assert get_available_python_envs('unkown') == None, 'unknown env manager'

"""Tests for the module run_commands.py."""

from pathlib import Path
from json import dumps
from typing import Generator
from pytest_subprocess.fixtures import fp, FakeProcess

from app.solve.envs.managers import EnvManager
from app.solve.envs.run_commands import get_environment_run_command
from app.solve.envs.managers import get_installed_python_env_managers
from app.solve.envs.python_envs import get_available_python_envs


def test_get_environment_run_command(
        fp: Generator[FakeProcess, None, None],
    ) -> None:
    """"""
    # FIRST TEST: success

    # for get_installed_python_env_managers
    fp.register([EnvManager.CONDA, '--version'], returncode=0) #type: ignore
    fp.register([EnvManager.MAMBA, '--version'], returncode=0) #type: ignore

    # for get_available_python_envs
    cmd = [EnvManager.CONDA, 'env', 'list', '--json']
    stdout = {
        'envs': [
            '/path/to/base',
            '/path/to/envs/env_1',
            '/path/to/envs/env_2',
        ]
    }
    fp.register(cmd, dumps(stdout), returncode=0) #type: ignore

    assert get_environment_run_command(
        Path('pypsa_earth_folder_path'),
        get_installed_python_env_managers,
        get_available_python_envs
    ) == f"conda run -n env_1 --cwd pypsa_earth_folder_path", 'first test'


    # SECOND TEST: no python env managers installed

    # for get_installed_python_env_managers
    fp.register([EnvManager.CONDA, '--version'], returncode=127) #type: ignore
    fp.register([EnvManager.MAMBA, '--version'], returncode=127) #type: ignore

    assert get_environment_run_command(
        Path('pypsa_earth_folder_path'),
        get_installed_python_env_managers,
        get_available_python_envs
    ) == None, 'second test'


    # THIRD TEST: error on subprocess of get_available_python_envs

    # for get_installed_python_env_managers
    fp.register([EnvManager.CONDA, '--version'], returncode=0) #type: ignore
    fp.register([EnvManager.MAMBA, '--version'], returncode=0) #type: ignore

    # for get_available_python_envs
    cmd = [EnvManager.CONDA, 'env', 'list', '--json']
    stdout = {
        'envs': [
            '/path/to/base',
            '/path/to/envs/env_1',
            '/path/to/envs/env_2',
        ]
    }
    fp.register(cmd, dumps(stdout), returncode=1) #type: ignore

    assert get_environment_run_command(
        Path('pypsa_earth_folder_path'),
        get_installed_python_env_managers,
        get_available_python_envs
    ) == None, 'third test'

    # FORTH TEST: python environment manager neither conda nor mamba.

    # for get_installed_python_env_managers
    fp.register(['unknown', '--version'], returncode=0) #type: ignore
    fp.register([EnvManager.CONDA, '--version'], returncode=127) #type: ignore
    fp.register([EnvManager.MAMBA, '--version'], returncode=127) #type: ignore

    # for get_available_python_envs
    cmd = [EnvManager.CONDA, 'env', 'list', '--json']
    stdout = {
        'envs': [
            '/path/to/base',
            '/path/to/envs/env_1',
            '/path/to/envs/env_2',
        ]
    }
    fp.register(cmd, dumps(stdout), returncode=1) #type: ignore

    assert get_environment_run_command(
        Path('pypsa_earth_folder_path'),
        get_installed_python_env_managers,
        get_available_python_envs
    ) == None, 'forth test'

    # FIFTH TEST: no python environment availables.

    # for get_installed_python_env_managers
    fp.register([EnvManager.CONDA, '--version'], returncode=0) #type: ignore
    fp.register([EnvManager.MAMBA, '--version'], returncode=0) #type: ignore

    # for get_available_python_envs
    cmd = [EnvManager.CONDA, 'env', 'list', '--json']
    stdout = {}
    fp.register(cmd, dumps(stdout), returncode=1) #type: ignore

    assert get_environment_run_command(
        Path('pypsa_earth_folder_path'),
        get_installed_python_env_managers,
        get_available_python_envs
    ) == None, 'fifth test'



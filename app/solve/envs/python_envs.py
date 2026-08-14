"""Python environments.

This module provide resources to retrieve existing local python environments.

Functions
---------
get_available_python_envs(python_env_mngr: str) -> list[str] | None \\
"""

from json import loads
from subprocess import run

from app.solve.envs.env_managers import EnvManager


def get_available_python_envs(python_env_mngr: str) -> list[str] | None:
    """Get the list of available python environments for python_env_mngr.
    
    Accepted python_env_mngr values are conda or mamba. The command executed
    via subprocess.run() is 'python_env_mngr env list --json', which returns
    the list of environments in json format.

    The list of envs is thus extracted using 'json_result.get("envs")', which
    is then split entry by entry using '/' if 'envs' is present in the path (to
    discard the base environment). For example:

    json_result = {
        'envs': ['/path/to/base','/path/to/envs/env_1', '/path/to/envs/env_2']
    }

    returns ['env_1', 'env_2'].

    Parameters
    ----------
    python_env_mngr: str
        The name of the python environment manager.

    Returns
    -------
    list[str] | None
        A list with the names of the python_env_mngr's environments available.
        None in case (a) an error happens on invoking subprocess.run() or (b)
        python_env_mngr not in ('conda', 'mamba').
    """
    if python_env_mngr in EnvManager.to_list():
        result = run(
            [python_env_mngr, 'env', 'list', '--json'], # return in json format
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            envs = loads(result.stdout).get('envs', [])
            if len(envs) > 0:
                return [env.split('/')[-1] for env in envs if 'envs' in env]
            return []
    return None

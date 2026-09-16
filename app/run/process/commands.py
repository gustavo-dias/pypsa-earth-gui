"""PyPSA-Earth solve commands.

This module provides a function to build valid PyPSA-Earth solve commands.

Functions
---------
get_solve_command(env_cmd: str, snakemake_cmd: str) -> str
"""

def get_solve_command(env_cmd: str, snakemake_cmd: str) -> str:
    """Get the PyPSA-Earth solve process command.
    
    Format: 'env_cmd -- snakemake_cmd'

    Parameters
    ----------
    env_cmd: str
        The python env manager run command. 
    snakemake_cmd: str
        The snakemake run command.
    
    Returns
    -------
    str
        A string representing the solve command.
    """
    return f"{env_cmd} -- {snakemake_cmd}"

"""Snakemake rules.

This module provides a function that extracts solve rules from PyPSA-Earth's 
snakemake file.

Functions
---------
get_snakemake_rules(pypsa_earth_folder_path: Path) -> list[str]
"""

from re import compile
from pathlib import Path


def get_snakemake_rules(pypsa_earth_folder_path: Path) -> list[str]:
    """Get the snakemake solve rules in pypsa_earth_folder_path.
    
    The function searchs solve rules in PyPSA-Earth's snakemake file using the
    regex 'solve_[a-z_A-Z]*'. It returns a list with unique values, i.e., if
    there are two identical matches, only one match is returned. For example,
    in the extract below there are two 'solve_network' rules, so only one 
    'solve_network' entry is present in the returning list.
    __
    rule solve_network:
        ...
    
    rule solve_all:
        rule solve_network:
            ...
    ___

    Parameters
    ----------
    pypsa_earth_folder_path: Path
        The path to the local PyPSA-Earth installation.

    Returns
    -------
    list[str]
        A list containing the available solve rules.
    """
    rules: list[str] = []
    with open(Path(pypsa_earth_folder_path, 'Snakefile'), 'r') as file:
        rules = list(set(compile('solve_[a-z_A-Z]*').findall(file.read())))
        rules.sort()
    return rules

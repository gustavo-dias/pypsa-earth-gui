"""Tests for module commands.py."""

from app.solve.process.commands import get_solve_command

def test_get_solve_command() -> None:
    """"""
    assert get_solve_command('', '') == ' -- ', 'blank'

    assert get_solve_command(
        'conda run -n pypsa-earth',
        'snakemake -j 1 solve_network'
    ) == 'conda run -n pypsa-earth -- snakemake -j 1 solve_network', 'full cmd'
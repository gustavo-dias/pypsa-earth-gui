"""Tests for module snakemake/run_commands.py."""

from pathlib import Path
from pytest_mock import MockerFixture

from app.run.snakemake.commands import get_snakemake_command
from app.run.snakemake.rules import get_snakemake_solve_rules


def test_get_snakemake_command(snakemake_file: MockerFixture) -> None:
    """"""

    assert get_snakemake_command(Path(''), get_snakemake_solve_rules) == \
        "snakemake -j 1 solve_all"
"""Tests for the module rules.py."""

from pathlib import Path
from pytest_mock import MockerFixture

from app.solve.snakemake.rules import get_snakemake_rules

def test_get_snakemake_rules(snakemake_file: MockerFixture) -> None:
    """"""
    assert get_snakemake_rules(Path("")) == ['solve_all', 'solve_some']
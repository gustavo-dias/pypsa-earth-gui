"""Tests for module termination.py."""

from typing import Generator
# from subprocess import Popen

# from app.solve.process.termination import kill_process
from pytest_subprocess.fixtures import fp, FakeProcess


def test_kill_process(fp: Generator[FakeProcess, None, None]) -> None:
    """"""
    # TODO: make idea below work
    # fp.register(['sleep', '200']) # type: ignore
    # process = Popen(['sleep', '200'], text=True)
    # assert kill_process(process)
    pass
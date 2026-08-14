"""Tests for module execution.py."""

from subprocess import Popen

from app.solve.process.execution import get_subprocess_for

def test_get_subprocess_for() -> None:
    """"""
    assert type(get_subprocess_for('sleep --version')) == Popen, 'type'

    process = get_subprocess_for('sleep --version')
    if process is not None:
        process.communicate()
        assert process.returncode == 0, 'finished no error'

    assert get_subprocess_for('unkown 80') == None, 'None'
"""Tests for the module monitoring.py."""

from time import time

from app.solve.process.monitoring import is_timed_out


def test_monitor_process() -> None:
    """"""
    # TODO: check why monitor_process is returning None
    # fp.register(['sleep', '120']) # type: ignore
    # process = Popen(
    #     ['sleep', '120'],
    #     start_new_session=True,
    #     stdout=PIPE,
    #     stderr=STDOUT,
    #     text=True,
    # )
    # t, v = monitor_process(process, 1, time(), is_timed_out, kill_solve_process)
    pass


def test_is_timed_out() -> None:
    """"""
    time_out = 0 # 0 minutes => inactive
    assert is_timed_out(time_out, time()) == False, 'time out not active'

    time_out = 1 # one minute => active
    assert is_timed_out(time_out, time()) == False, 'not timed out'

    assert is_timed_out(time_out, time()-(time_out*66.0)) == True, 'timed out'
import time

import pytest

from tasks.decorators import memoize, retry, shout, timer, trace, validate_ip


# ---------- 1. shout ----------

def test_01_shout():
    @shout
    def greet(name, greeting="hello"):
        """Greet someone."""
        return f"{greeting}, {name}"

    assert greet("ivan") == "HELLO, IVAN"
    assert greet("ivan", greeting="hi") == "HI, IVAN"
    assert greet.__name__ == "greet"
    assert greet.__doc__ == "Greet someone."


def test_01_shout_no_args():
    @shout
    def status():
        return "up"

    assert status() == "UP"


# ---------- 2. trace ----------

def test_02_trace(capsys):
    @trace
    def add(a, b):
        return a + b

    assert add(2, 3) == 5
    out = capsys.readouterr().out
    assert out == "-> add\n<- add\n"


def test_02_trace_keeps_name():
    @trace
    def add(a, b):
        return a + b

    assert add.__name__ == "add"


# ---------- 3. timer ----------

def test_03_timer():
    @timer
    def slow(delay):
        time.sleep(delay)
        return "done"

    assert slow.last_duration is None
    assert slow(0.05) == "done"
    assert 0.05 <= slow.last_duration < 1


def test_03_timer_updates_every_call():
    @timer
    def slow(delay):
        time.sleep(delay)

    slow(0.05)
    first = slow.last_duration
    slow(0)
    assert slow.last_duration < first


# ---------- 4. validate_ip ----------

def test_04_validate_ip_valid():
    @validate_ip
    def ping(ip, count=1):
        return f"ping {ip} x{count}"

    assert ping("10.0.0.1") == "ping 10.0.0.1 x1"
    assert ping("10.0.0.1", count=3) == "ping 10.0.0.1 x3"


@pytest.mark.parametrize("ip", ["999.0.0.1", "abc", "1.2.3", ""])
def test_04_validate_ip_invalid(ip):
    calls = []

    @validate_ip
    def ping(ip):
        calls.append(ip)

    with pytest.raises(ValueError):
        ping(ip)
    assert calls == [], "the function must not be called with a bad IP"


# ---------- 5. memoize ----------

def test_05_memoize_calls_once():
    calls = []

    @memoize
    def resolve(host):
        calls.append(host)
        return f"ip-of-{host}"

    assert resolve("a.local") == "ip-of-a.local"
    assert resolve("a.local") == "ip-of-a.local"
    assert calls == ["a.local"]


def test_05_memoize_different_args():
    calls = []

    @memoize
    def add(a, b):
        calls.append((a, b))
        return a + b

    assert add(1, 2) == 3
    assert add(2, 1) == 3
    assert add(1, 2) == 3
    assert calls == [(1, 2), (2, 1)]
    assert add.cache == {(1, 2): 3, (2, 1): 3}


# ---------- 6. retry ----------

def make_flaky(fail_times):
    """Return a function that fails `fail_times` times, then returns "ok"."""
    attempts = []

    def connect():
        attempts.append(1)
        if len(attempts) <= fail_times:
            raise ConnectionError(f"attempt {len(attempts)} failed")
        return "ok"

    return connect, attempts


def test_06_retry_success_after_failures():
    connect, attempts = make_flaky(fail_times=2)
    assert retry(times=3)(connect)() == "ok"
    assert len(attempts) == 3


def test_06_retry_first_try():
    connect, attempts = make_flaky(fail_times=0)
    assert retry(times=3)(connect)() == "ok"
    assert len(attempts) == 1


def test_06_retry_all_fail_raises_last():
    connect, attempts = make_flaky(fail_times=5)
    with pytest.raises(ConnectionError, match="attempt 3 failed"):
        retry(times=3)(connect)()
    assert len(attempts) == 3


def test_06_retry_with_args_and_name():
    @retry(times=2)
    def add(a, b=0):
        """Add numbers."""
        return a + b

    assert add(2, b=3) == 5
    assert add.__name__ == "add"
    assert add.__doc__ == "Add numbers."

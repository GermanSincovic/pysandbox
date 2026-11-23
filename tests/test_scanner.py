import pytest

from tasks.scanner import PortScanner, summarize


@pytest.fixture
def scanner():
    s = PortScanner("10.0.0.1")
    s.add_result(443, "open")
    s.add_result(80, "closed")
    s.add_result(22, "open")
    return s


def test_get_status(scanner):
    assert scanner.get_status(22) == "open"
    assert scanner.get_status(80) == "closed"


def test_get_status_unknown(scanner):
    assert scanner.get_status(8080) == "unknown"


def test_open_ports_sorted(scanner):
    assert scanner.open_ports() == [22, 443]


@pytest.mark.parametrize("status, expected", [("open", 2), ("closed", 1), ("filtered", 0)])
def test_count(scanner, status, expected):
    assert scanner.count(status) == expected


def test_summarize():
    results = [
        ("10.0.0.1", 22, "open"),
        ("10.0.0.1", 80, "closed"),
        ("10.0.0.2", 443, "open"),
        ("10.0.0.1", 443, "open"),
        ("10.0.0.3", 22, "closed"),
    ]
    assert summarize(results) == {"10.0.0.1": 2, "10.0.0.2": 1, "10.0.0.3": 0}


def test_summarize_empty():
    assert summarize([]) == {}

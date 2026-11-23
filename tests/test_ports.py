import pytest

from tasks.ports import parse_ports, validate_port


@pytest.mark.parametrize("value, expected", [
    pytest.param("443", 443, id="string"),
    pytest.param(22, 22, id="int"),
    pytest.param(" 80 ", 80, id="spaces"),
    pytest.param("1", 1, id="min"),
    pytest.param(65535, 65535, id="max"),
])
def test_validate_port_valid(value, expected):
    assert validate_port(value) == expected


@pytest.mark.parametrize("value", [
    pytest.param("abc", id="not_number"),
    pytest.param("", id="empty"),
    pytest.param("0", id="zero"),
    pytest.param(65536, id="above_max"),
    pytest.param("-1", id="negative"),
])
def test_validate_port_invalid(value):
    with pytest.raises(ValueError):
        validate_port(value)


@pytest.mark.parametrize("text, expected", [
    pytest.param("443, 22,80, 22", [22, 80, 443], id="duplicates"),
    pytest.param(" 8080 ,abc, 21 ", [21, 8080], id="garbage"),
    pytest.param("", [], id="empty"),
])
def test_parse_ports(text, expected):
    assert parse_ports(text) == expected

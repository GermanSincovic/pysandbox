import pytest

from tasks.ip_tools import is_valid_ipv4, network_info, same_subnet


@pytest.mark.parametrize("ip, expected", [
    pytest.param("192.168.1.1", True, id="valid"),
    pytest.param("0.0.0.0", True, id="all_zero"),
    pytest.param("255.255.255.255", True, id="all_max"),
    pytest.param("256.1.1.1", False, id="above_255"),
    pytest.param("1.2.3", False, id="three_parts"),
    pytest.param("1.2.3.4.5", False, id="five_parts"),
    pytest.param("01.2.3.4", False, id="leading_zero"),
    pytest.param("1..2.3", False, id="empty_part"),
    pytest.param("a.b.c.d", False, id="letters"),
    pytest.param("", False, id="empty"),
])
def test_is_valid_ipv4(ip, expected):
    assert is_valid_ipv4(ip) == expected


@pytest.mark.parametrize("cidr, expected", [
    pytest.param("192.168.1.70/26", {"network": "192.168.1.64", "broadcast": "192.168.1.127", "hosts": 62},
                 id="slash26"),
    pytest.param("10.0.0.200/28", {"network": "10.0.0.192", "broadcast": "10.0.0.207", "hosts": 14},
                 id="slash28"),
    pytest.param("172.16.5.37/24", {"network": "172.16.5.0", "broadcast": "172.16.5.255", "hosts": 254},
                 id="slash24"),
])
def test_network_info(cidr, expected):
    assert network_info(cidr) == expected


@pytest.mark.parametrize("ip1, ip2, prefix, expected", [
    pytest.param("10.0.1.20", "10.0.1.200", 24, True, id="same_24"),
    pytest.param("192.168.1.50", "192.168.1.70", 26, False, id="different_26"),
    pytest.param("192.168.1.100", "192.168.1.120", 27, True, id="same_27"),
    pytest.param("10.0.0.1", "10.1.0.1", 16, False, id="different_16"),
])
def test_same_subnet(ip1, ip2, prefix, expected):
    assert same_subnet(ip1, ip2, prefix) == expected

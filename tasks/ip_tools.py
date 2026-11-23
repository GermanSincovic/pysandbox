def is_valid_ipv4(ip):
    """Check an IPv4 address WITHOUT any libraries.

    Rules: 4 parts separated by dots, each part is a number 0-255,
    no leading zeros ("01" is invalid), no empty parts.

    is_valid_ipv4("192.168.1.1") -> True
    is_valid_ipv4("256.1.1.1")   -> False
    is_valid_ipv4("1.2.3")       -> False
    is_valid_ipv4("01.2.3.4")    -> False
    """
    raise NotImplementedError


def network_info(cidr):
    """Return network info for a CIDR string. Use the ipaddress module.

    network_info("192.168.1.70/26") -> {
        "network": "192.168.1.64",
        "broadcast": "192.168.1.127",
        "hosts": 62,
    }
    Hint: ipaddress.ip_network(cidr, strict=False)
    """
    raise NotImplementedError


def same_subnet(ip1, ip2, prefix):
    """Return True if both IPs are in the same subnet with this prefix length.

    same_subnet("10.0.1.20", "10.0.1.200", 24) -> True
    same_subnet("192.168.1.50", "192.168.1.70", 26) -> False
    """
    raise NotImplementedError

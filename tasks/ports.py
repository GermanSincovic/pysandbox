def validate_port(value):
    """Return the port as int if it is a valid port (1-65535).

    Accepts a string or an int. Raises ValueError otherwise.

    validate_port("443")  -> 443
    validate_port(22)     -> 22
    validate_port(" 80 ") -> 80
    validate_port("abc")  -> ValueError
    validate_port(70000)  -> ValueError
    """
    raise NotImplementedError


def parse_ports(text):
    """Parse comma separated ports into a sorted list of unique ints.

    Skip everything that is not a number.

    parse_ports("443, 22,80, 22")  -> [22, 80, 443]
    parse_ports(" 8080 ,abc, 21 ") -> [21, 8080]
    parse_ports("")                -> []
    """
    raise NotImplementedError

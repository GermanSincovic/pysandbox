class PortScanner:
    """Store scan results for one host.

    scanner = PortScanner("10.0.0.1")
    scanner.add_result(22, "open")
    scanner.add_result(80, "closed")
    scanner.get_status(22)   -> "open"
    scanner.get_status(8080) -> "unknown"
    scanner.open_ports()     -> [22]         (sorted)
    scanner.count("open")    -> 1
    """

    def __init__(self, ip):
        raise NotImplementedError

    def add_result(self, port, status):
        raise NotImplementedError

    def get_status(self, port):
        raise NotImplementedError

    def open_ports(self):
        raise NotImplementedError

    def count(self, status):
        raise NotImplementedError


def summarize(results):
    """Count open ports per IP.

    results is a list of tuples (ip, port, status).
    Hosts without open ports must be in the result with 0.

    summarize([("10.0.0.1", 22, "open"), ("10.0.0.2", 80, "closed")])
        -> {"10.0.0.1": 1, "10.0.0.2": 0}
    """
    raise NotImplementedError

class WordCounter:
    """The live coding task from the interview.

    wc = WordCounter()
    wc.add_word("apple")
    wc.add_word("apple")
    wc.get_count("apple")    -> 2
    wc.get_count("cucumber") -> 0
    """

    def __init__(self):
        raise NotImplementedError

    def add_word(self, word):
        raise NotImplementedError

    def get_count(self, word):
        raise NotImplementedError


def top_ips(lines, n):
    """Return the n most frequent IPs from access log lines.

    The IP is the first field of each line. Skip empty lines.
    Return a list of (ip, count) tuples, the most frequent first.

    top_ips(["10.0.0.1 GET /", "10.0.0.2 GET /", "10.0.0.1 GET /a"], 1)
        -> [("10.0.0.1", 2)]
    """
    raise NotImplementedError


def chunks(items, size):
    """Generator: yield the list in parts of `size` elements. Use yield.

    list(chunks([1, 2, 3, 4, 5], 2)) -> [[1, 2], [3, 4], [5]]
    list(chunks([1, 2, 3, 4], 2))    -> [[1, 2], [3, 4]]   (no empty tail!)
    list(chunks([], 3))              -> []
    """
    raise NotImplementedError

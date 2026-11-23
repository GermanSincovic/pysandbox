"""Python basics. Solve the tasks in order, from 1 to 14."""


# ---------- Strings ----------

def reverse_words(text):
    """1. Reverse the order of words.

    reverse_words("show ip route") -> "route ip show"
    reverse_words("  a   b ")      -> "b a"
    Hint: split() and " ".join()
    """
    raise NotImplementedError


def is_palindrome(text):
    """2. Check palindrome ignoring case and everything that is not a letter or digit.

    is_palindrome("Level")                 -> True
    is_palindrome("A man, a plan, a canal: Panama") -> True
    is_palindrome("router")                -> False
    Hint: str.isalnum(), str.lower(), slicing [::-1]
    """
    raise NotImplementedError


# ---------- Dicts and sets ----------

def char_frequency(text):
    """3. Count every character except spaces.

    char_frequency("aab b") -> {"a": 2, "b": 2}
    Hint: d[key] = d.get(key, 0) + 1
    """
    raise NotImplementedError


def unique_sorted(items):
    """4. Return sorted list of unique items.

    unique_sorted([3, 1, 3, 2, 1]) -> [1, 2, 3]
    Hint: set()
    """
    raise NotImplementedError


def merge_counts(a, b):
    """5. Merge two dicts with counts: values of common keys are summed.

    Do not change the input dicts.

    merge_counts({"x": 1, "y": 2}, {"y": 3, "z": 4}) -> {"x": 1, "y": 5, "z": 4}
    """
    raise NotImplementedError


def group_by_length(words):
    """6. Group words by their length.

    group_by_length(["ssh", "dns", "http", "ntp"]) -> {3: ["ssh", "dns", "ntp"], 4: ["http"]}
    Hint: dict.setdefault(key, []).append(...)
    """
    raise NotImplementedError


# ---------- Lists, comprehension, sorting ----------

def flatten(nested):
    """7. Flatten a list of lists (one level). Try a list comprehension.

    flatten([[1, 2], [3], []]) -> [1, 2, 3]
    """
    raise NotImplementedError


def sort_devices(devices):
    """8. Sort devices by "vlan" (ascending), then by "name" (alphabetical).

    Return a NEW list, do not change the input.
    Hint: sorted(..., key=lambda d: (d["vlan"], d["name"]))
    """
    raise NotImplementedError


# ---------- Functions ----------

def add_item(item, items=None):
    """9. Append item to items and return the list.

    If items is not given, start with a NEW empty list on every call.
    add_item(1) -> [1]
    add_item(2) -> [2]        (not [1, 2]!)
    """
    raise NotImplementedError


def build_url(host, *path, **params):
    """10. Build a URL from parts.

    build_url("api.local")                          -> "https://api.local"
    build_url("api.local", "v1", "alarms")          -> "https://api.local/v1/alarms"
    build_url("api.local", "v1", limit=10, page=2)  -> "https://api.local/v1?limit=10&page=2"
    Params keep the order they were given in.
    """
    raise NotImplementedError


# ---------- Exceptions ----------

def safe_divide(a, b):
    """11. Return a / b, or None if b is zero. Use try/except, not if.

    safe_divide(10, 4) -> 2.5
    safe_divide(1, 0)  -> None
    """
    raise NotImplementedError


# ---------- Classes ----------

class Vlan:
    """12. A VLAN with id and name.

    - vid must be 1-4094, otherwise raise ValueError
    - repr(Vlan(10, "users")) -> "Vlan(10, 'users')"
    - two Vlan objects are equal if their vid is equal
    - Vlan objects can be put into a set (implement __hash__)
    """

    def __init__(self, vid, name):
        raise NotImplementedError


# ---------- Generators ----------

def even_squares(limit):
    """13. Generator: yield squares of even numbers from 0 up to (not including) limit.

    list(even_squares(7)) -> [0, 4, 16, 36]
    Use yield.
    """
    raise NotImplementedError


# ---------- Decorators ----------

def count_calls(func):
    """14. Decorator that counts calls of the function.

    @count_calls
    def ping(): ...
    ping(); ping()
    ping.calls      -> 2
    ping.__name__   -> "ping"   (use functools.wraps)
    The decorated function must return the original result.
    """
    raise NotImplementedError

"""Python basics. Solve the tasks in order, from 1 to 14."""

# ---------- Strings ----------
import functools
import re


def reverse_words(text):
    return " ".join(reversed([x.strip() for x in str(text).split()]))


def is_palindrome(text):
    pattern = re.compile("\\W", flags=re.MULTILINE)
    clean_text = pattern.sub("", text).lower()
    return clean_text == clean_text[::-1]


# ---------- Dicts and sets ----------

def char_frequency(text):
    res = {}
    for sym in text:
        if sym != " ":
            res[sym] = res.get(sym, 0) + 1
    return res


def unique_sorted(items):
    return sorted(list(set(items)))


def merge_counts(a, b):
    res = dict.copy(a)
    for k, v in b.items():
        res[k] = res.get(k, 0) + v
    return res


def group_by_length(words):
    res = {}
    for w in words:
        res.setdefault(len(w), []).append(w)
    return res


# ---------- Lists, comprehension, sorting ----------

def flatten(nested):
    return [y for x in nested for y in x]


def sort_devices(devices):
    return sorted(devices, key=lambda d: (d["vlan"], d["name"]))


# Too obvious hint


# ---------- Functions ----------

def add_item(item, items=None):
    if items is not None:
        items.append(item)
        return items
    else:
        return [item]


def build_url(host, *path, **params):
    proto = "https://"
    if proto not in host:
        host = proto + host
    if len(path) > 0:
        host += "/" + "/".join(p for p in path)
    if len(params.keys()) > 0:
        host += "?" + "&".join(["=".join([str(k), str(v)]) for k, v in params.items()])
    return host


# ---------- Exceptions ----------

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


# ---------- Classes ----------

class Vlan:

    def __init__(self, vid, name):
        if vid in range(1, 4095):
            self.vid = vid
        else:
            raise ValueError
        self.name = name

    def __repr__(self):
        return f"Vlan({self.vid}, '{self.name}')"

    def __eq__(self, other) -> bool:
        if type(other) is type(self):
            return self.vid == other.vid
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.vid)


# ---------- Generators ----------

def even_squares(limit):
    for x in range(limit):
        square = x ** 2
        if square % 2 == 0:
            yield square


# ---------- Decorators ----------

def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper

"""Python basics. Solve the tasks in order, from 1 to 14."""

# ---------- Strings ----------
import functools
import re


def reverse_words(text):
    return " ".join(text.split(" ").reverse())


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
    return list(set(items)).sort()


def merge_counts(a, b):
    res = dict.copy(a)
    for k, v in b.items():
        res[k] = res.get(k, 0) + 1
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
    return devices.sorted(devices, key=lambda d: (d["vlan"], d["name"]))


# Too obvious hint


# ---------- Functions ----------

def add_item(item, items=None):
    if items and items is list:
        return list(items).append(item)
    else:
        return [item]


def build_url(host, *path, **params):
    url = "/".join([host, (p for p in path)])
    url += "?"
    url += "&".join(["=".join([k, v]) for k, v in params])
    return url


# ---------- Exceptions ----------

def safe_divide(a, b):
    try:
        return a / b
    except ValueError:
        return None


# ---------- Classes ----------

class Vlan:

    def __init__(self, vid, name):
        if id in range(1, 4095):
            self.vid = id
        else:
            raise ValueError
        self.name = name

    def __repr__(self):
        return f"{self.__name__}({self.vid}, {self.name})"

    def __eq__(self, other) -> bool:
        if type(other) is type(self):
            return self.vid == other.vid
        else:
            return False

    def __hash__(self) -> int:
        return hash((self.vid, self.name))


# ---------- Generators ----------

def even_squares(limit):
    for x in range(limit):
        if x ** limit % 2 == 0:
            yield x ** limit


# ---------- Decorators ----------

def count_calls(func):
    i = 0

    @functools.wraps(func)
    def wrapper():
        func()
        print("Function called", i + 1, "times")

"""Decorators. Solve in order, from 1 to 6.

Every decorator must:
- work with ANY function (any positional and keyword arguments),
- return the result of the original function (unless the task says otherwise),
- keep the original name and docstring (functools.wraps).

Skeleton:

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # something before
            result = func(*args, **kwargs)
            # something after
            return result
        return wrapper
"""
import functools
import time


def shout(func):
    """1. Return the result of the function in UPPER CASE.

    @shout
    def greet(name, greeting="hello"):
        return f"{greeting}, {name}"

    greet("ivan")                 -> "HELLO, IVAN"
    greet("ivan", greeting="hi")  -> "HI, IVAN"
    """
    raise NotImplementedError


def trace(func):
    """2. Print a line before and after the call.

    @trace
    def add(a, b):
        return a + b

    add(2, 3) prints:
        -> add
        <- add
    and returns 5.
    Hint: func.__name__ is the name of the function.
    """
    raise NotImplementedError


def timer(func):
    """3. Measure how long the call took.

    Save the duration in seconds (float) into the wrapper attribute
    `last_duration` after every call. Before the first call it is None.

    @timer
    def slow():
        time.sleep(0.05)

    slow.last_duration  -> None
    slow()
    slow.last_duration  -> about 0.05
    Hint: time.perf_counter()
    """
    raise NotImplementedError


def validate_ip(func):
    """4. Check that the FIRST argument of the function is a valid IPv4 address.

    If it is not, raise ValueError and do NOT call the function.

    @validate_ip
    def ping(ip, count=1):
        return f"ping {ip} x{count}"

    ping("10.0.0.1", count=3) -> "ping 10.0.0.1 x3"
    ping("999.0.0.1")         -> ValueError
    Hint: ipaddress.IPv4Address(...) raises ValueError for a bad address.
    """
    raise NotImplementedError


def memoize(func):
    """5. Cache results: for the same arguments call the function only once.

    Store the cache in the wrapper attribute `cache` (a dict).
    Only positional arguments are used (no kwargs).

    @memoize
    def resolve(host):
        ...  # slow DNS lookup

    resolve("a.local")   # calls the function
    resolve("a.local")   # returns cached result, the function is NOT called
    resolve.cache        -> {("a.local",): <result>}
    Hint: args is a tuple, so it can be a dict key.
    """
    raise NotImplementedError


def retry(times):
    """6. Decorator WITH a parameter: retry the function if it raises an exception.

    Call the function up to `times` times in total. If it succeeds, return the result.
    If all attempts fail, raise the LAST exception.

    @retry(times=3)
    def connect():
        ...

    This needs THREE levels of functions:
        retry(times) -> decorator(func) -> wrapper(*args, **kwargs)
    Remember: @retry(times=3) first CALLS retry(times=3),
    and what it returns is applied to the function.
    """
    raise NotImplementedError

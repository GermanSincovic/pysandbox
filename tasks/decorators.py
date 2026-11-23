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
import ipaddress
import time


def shout(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return str(res).upper()

    return wrapper


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("-> add")
        print("<- add")
        return func(*args, **kwargs)

    return wrapper


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        wrapper.last_duration = time.perf_counter() - start
        return res

    wrapper.last_duration = None
    return wrapper


def validate_ip(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print(ipaddress.IPv4Address(args[0]))
        except ValueError:
            raise ValueError("the function must not be called with a bad IP")
        else:
            return func(*args, **kwargs)

    return wrapper


def memoize(func):
    @functools.wraps(func)
    def wrapper(*args):
        res = wrapper.cache.get(args, None)
        if res is not None:
            return res
        else:
            res = func(*args)
            wrapper.cache[args] = res
            return res

    wrapper.cache = {}
    return wrapper


def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for n in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if n == times:
                        raise

        return wrapper

    return decorator

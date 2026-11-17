import functools
import time


def timer(threshold=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            try:
                return func(*args, **kwargs)
            finally:
                duration = time.perf_counter() - start
                if duration > 2:
                    print(f"WARNING! Duration took more then {threshold} s")
        return wrapper
    return decorator


@timer
def ping_all(ips): ...

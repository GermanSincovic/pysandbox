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
                if duration > threshold:
                    print(f"WARNING! Duration took more then {threshold} s")

        return wrapper

    return decorator


@timer
def ping_all(ips): ...


#############################

def parse_interfaces(output: str):
    if output == "" or output is None:
        return None
    result = {}
    for line in output.split(sep="\n")[1::]:
        chunks = line.split()
        for chunk in chunks:
            if chunk == "unassigned":
                chunk = None
            result.update({"name": chunk})
            result.update({"ip": chunk})
            result.update({"status": chunk})
            result.update({"protocol": chunk})
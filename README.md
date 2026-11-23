# pysandbox

Python practice tasks with pytest tests.

## Structure

```
tasks/          # code: one file per task
tests/          # tests: test_<task>.py for each task
pytest.ini      # pytest settings (where tests are, import path)
requirements.txt
```

## Tasks

Every task is a function or class stub that raises `NotImplementedError`.
Write the code, run the tests. Tests of unsolved tasks are shown as SKIPPED,
so the run stays green until you start a task.

Suggested order:

| File | Topic | Tests |
|---|---|---|
| `tasks/basics.py` | Python basics: strings, dicts, sets, lists, sorting, functions, exceptions, classes, generators, decorators (tasks 1-14) | `tests/test_basics.py` |
| `tasks/decorators.py` | decorators: wrapper, `*args/**kwargs`, `functools.wraps`, attributes on wrapper, decorator with parameter (tasks 1-6) | `tests/test_decorators.py` |
| `tasks/ports.py` | validate and parse ports, exceptions | `tests/test_ports.py` |
| `tasks/scanner.py` | class with a dict, counting | `tests/test_scanner.py` |
| `tasks/logs.py` | WordCounter, top IPs from logs, chunks generator | `tests/test_logs.py` |
| `tasks/ip_tools.py` | IPv4 validation, subnets with `ipaddress` | `tests/test_ip_tools.py` |
| `tasks/interfaces.py` | parse `show interfaces` output (solved) | `tests/test_interfaces.py` |

Work on one task at a time:

```bash
pytest tests/test_basics.py -k 01     # only task 1 of basics
pytest tests/test_ports.py            # one file
```

## Run tests from terminal

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest
```

Useful options:

```bash
pytest tests/test_interfaces.py     # one file
pytest -k unassigned                # tests whose name contains a word
pytest -x                           # stop on first failure
pytest --lf                         # rerun only last failed
```

## Run tests in PyCharm

1. Settings > Project > Python Interpreter: choose the `venv` interpreter of this project.
2. Settings > Tools > Python Integrated Tools > Default test runner: `pytest`.
3. Right click on the `tests` folder (or a test file) > Run 'pytest in tests'.

## CI

GitHub Actions runs `pytest` on every push (`.github/workflows/tests.yml`).

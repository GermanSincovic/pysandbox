# pysandbox

Python practice tasks with pytest tests.

## Structure

```
tasks/          # code: one file per task
tests/          # tests: test_<task>.py for each task
pytest.ini      # pytest settings (where tests are, import path)
requirements.txt
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

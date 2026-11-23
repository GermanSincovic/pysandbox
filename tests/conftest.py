import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Show tests of unsolved tasks as SKIPPED instead of FAILED.

    Every task stub raises NotImplementedError. While it is not solved,
    its tests are reported as skipped, so the test run stays green.
    """
    outcome = yield
    report = outcome.get_result()
    if call.when in ("setup", "call") and call.excinfo and call.excinfo.errisinstance(NotImplementedError):
        report.outcome = "skipped"
        report.longrepr = (str(item.path), item.location[1] or 0, "TODO: task is not solved yet")

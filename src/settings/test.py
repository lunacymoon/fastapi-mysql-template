import os


def pytest_scope_func() -> str:
    return os.getenv('PYTEST_CURRENT_TEST').split(' ')[0]


def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: mark a test as a smoke test.")
    config.addinivalue_line("markers", "regression: mark a test as a regression test.")
    config.addinivalue_line("markers", "slow: mark a test as slow.")
import pytest;

@pytest.fixture(scope="session")
def browser_setup():
    b = {"name": "Chrome", "version": "114.0.5735.199"}
    print(f"Setting up the browser: {b['name']} version {b['version']}")

    yield b  # Yield acts as a separator between before and after test execution. It will

    print(f"Tearing down the browser: {b['name']} version {b['version']}")

@pytest.fixture(scope="module")
def browser_page(browser_setup):
    page = {"url": "https://eaapp.somee.com", "title": "Employee Domain"}
    print(f"Setting up the page: {page['url']} with title '{page['title']}'")

    yield page  # Yield acts as a separator between before and after test execution. It will

    print(f"Tearing down the page: {page['url']} with title '{page['title']}'")
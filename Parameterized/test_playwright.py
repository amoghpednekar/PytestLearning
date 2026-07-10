import pytest;

# This is a parameterized test file for testing login functionality on different browsers and viewports. The test_login function takes two parameters, browser and viewport, which are defined using the parametrize decorator. The test function prints the browser and viewport being tested and asserts that the test passes.
@pytest.mark.parametrize("browser", 
                        ["Chrome", "Firefox", "Edge"])
@pytest.mark.parametrize("viewport",
                        ["Mobile", "Tablet", "Desktop"])

def test_login(browser,viewport):
    print(f"Testing login on {browser} with {viewport} viewport")
    assert True

# adding param as a list of tuples, where each tuple contains a browser and viewport combination. The test function takes two parameters, browser and viewport, which are defined using the parametrize decorator. The test function prints the browser and viewport being tested and asserts that the test passes.
@pytest.mark.parametrize("browser", 
                        [pytest.param("Chrome"),
                        pytest.param("Firefox"),
                        pytest.param("Edge"),
                        pytest.param("Safari", marks= pytest.mark.skip(reason="Safari is not supported"))
                        ])
@pytest.mark.parametrize("viewport",
                        ["Mobile", "Tablet", "Desktop"])

def test_setup_login(browser,viewport):
    print(f"Testing login on {browser} with {viewport} viewport")
    assert True
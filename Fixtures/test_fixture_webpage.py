import pytest;

@pytest.fixture #to resuse the same data in multiple test cases we can use fixture
def page_details():
    return {"title": "My Web Page", "url": "https://www.example.com", "author": "John Doe"}
@pytest.fixture
def environment_details():
    return {"env": "production", "browser": "Chrome", "version": "91.0", "os": "Apple M1"}

def test_page_title(page_details, environment_details):
    print(f"This is the test page title file for {page_details['title']} in {environment_details['env']} environment")
    print(f"Browser: {environment_details['browser']}, Version: {environment_details['version']}, OS: {environment_details['os']}")
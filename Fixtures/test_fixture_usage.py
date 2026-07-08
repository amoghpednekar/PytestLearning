import pytest;

@pytest.fixture #to resuse the same data in multiple test cases we can use fixture
def user():
    return {"name": "Alice", "age": 30, "city": "New York"}

def test_user_name(user):
    assert user["name"] == "Alice"
    print("This is the test user name file for {user['name']}")

def test_user_age(user):
    assert user["age"] == 30
    print("This is the test user age file for {user['age']}")

def test_user_city(user):
    assert user["city"] == "New York"
    print("This is the test user city file for {user['city']}")
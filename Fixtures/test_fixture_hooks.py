import pytest;

@pytest.fixture #to resuse the same data in multiple test cases we can use fixture
def db_connection():
    connection = "Database connection established"
    print(f"Connecting to the database: {connection}")

    yield connection  # Yield act as a seperator between before and after test execution. It will return the connection object to the test function

    connection = "Database connection closed"
    print(f"Disconnecting from the database: {connection}")

def test_db_connection(db_connection):
    assert db_connection == "Database connection established"
    print("This is the test database connection file")

def test_db_query(db_connection):
    assert db_connection == "Database connection established"
    print("This is the test database query file")
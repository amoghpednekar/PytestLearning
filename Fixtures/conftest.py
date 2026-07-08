import pytest;
import time

@pytest.fixture(scope="session") #to resuse the same data in multiple test cases we can use fixture
def db_connection():
    connection = "Database connection established"
    print(f"Connecting to the database: {connection}")
    time.sleep(2)  # Simulate a delay in establishing the connection
    yield connection  # Yield act as a seperator between before and after test execution. It will return the connection object to the test function

    connection = "Database connection closed"
    print(f"Disconnecting from the database: {connection}")
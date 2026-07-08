import pytest;

# scope="module" means the fixture will be created once per module, and the same instance will be used for all tests in that module. This is useful when you want to share expensive setup or teardown operations across multiple tests.
# scope="class" means the fixture will be created once per test class, and the same instance will be used for all tests in that class. This is useful when you want to share setup or teardown operations across multiple tests in a single class.
# scope="function" means the fixture will be created once per test function, and a new instance will be used for each test. This is useful when you want to isolate the setup or teardown operations for each test.
# scope="session" means the fixture will be created once per test session, and the same instance will be used for all tests in that session. This is useful when you want to share setup or teardown operations across multiple test modules or packages.

class TestDatabase:
    def test_db_connection(self, db_connection):
        assert db_connection == "Database connection established"
        print("This is the test database connection file")

    def test_db_query(self, db_connection):
        assert db_connection == "Database connection established"
        print("This is the test database query file")   

class TestDatabaseok:
    def test_db_connection(self, db_connection):
        assert db_connection == "Database connection established"
        print("This is the test database connection file test")

    def test_db_query(self, db_connection):
        assert db_connection == "Database connection established"
        print("This is the test database query file test")   
import pytest

def test_first():
    assert 1 + 1 == 2
    name1 =["Amogh:11", "Karthik:12", "Amo:13"]
    #assert "Amogh" in name1
    name2 = ["Amogh:32", "Karthik:12", "Amo:13"]
    assert name1 == name2
    print("This is the first test file")

def test_first_number_compare():
    assert 0.1 + 0.2 == pytest.approx(0.3)
    print("This is the first test number compare file")

def test_user_name():
    user = {
        "name": "Amogh",
        "age": 11,
        "city": "Pune"
    }
    assert user["name"] == "Amogh"
    assert user["age"] == 11
    print("This is the first test user name file for {user['name']}")

def test_text_compare():
    assert "hello" == "hello"
    print("This is the first test text file ")

def test_text_in_name(): #We should have test as the first part of the name
    assert "Amo" in "Among Us is a popular game"
    print("This is the first test text in name file")


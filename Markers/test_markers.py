import pytest;
import os
@pytest.mark.skip(reason="Skipping this test for demonstration purposes.")
def test_marker_example():
    assert 1==1
    print("This is a test marker example.")

#adding custom markers for smoke and regression tests but not using it in the test function
@pytest.mark.regression
def test_example_login():
    assert True
    print("This is a regression test example for login functionality.")

#marker test for xfail
@pytest.mark.xfail(reason="This is a known issue, Bug ID: #1234")

def test_fail_marker():
    assert 1==2
    print("this test is expected to fail due to a known issue.")

#adding custom markers and using it in the test function
@pytest.mark.smoke
@pytest.mark.slow
@pytest.mark.regression

def test_example_registration():
    assert 1==1
    print("This is a smoke, slow, and regression test example for registration functionality.")

# skip if the condition is true
@pytest.mark.skipif(os.getenv("API_KEY") is not "", reason="API_KEY environment variable is not set.")
def test_skipif_example():
    assert 1==1
    print("This test is skipped if the API_KEY environment variable is not set.")

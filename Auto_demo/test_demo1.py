# pytest method name should always start with test word.
# pytest file should start with test_ or end with _test.
# Any code should be wrapped in method only.
# Method name should have some sense.
# pytest marks can be used to skip or add custom marks to run that test.
# you can mark tests as pytest.mark.smoke and then run it with -m in pytest command
# You can skip test with pytest.mark.skip
# pytest.mark.xfail 
# conftest file is used to define all the fixtures in test suite
# autouse - Automatically use a fixture for every test function without explicitly mentioning.
# autouse is false by default.
# when scope is set to function, it is called once per test
# when scope is defined as a session, it runs once per test session.
# If the scope is set to class, the fixture will be called before each class only.
# if the scope is set to module, it will be called for once per file.
# finalizer fixture, end of all test methods like tear down.
# -k is to define keyword to execute that test.
# -m use to determine the mark give for test case eg login marker. (custom marker)
# xdist package is used to run the test in parallel using -n argument using that many num of workers.
# parametrize used to that enables you to run a single test function multiple times
# with different sets of input values.

import pytest

def test_m1():
    msg = "hello world"
    assert msg == "Hi", "TEST FAILED"

def test_m2():
    a = 3
    b = 4
    assert a == b, "a is not eq to b"
    assert a+1 == b, "test failed"

def test_m3():
    name = "selenium"
    assert name.upper() == "SELENIUM", "test failed"

@pytest.mark.login
def test_login():
    assert "admin" == "admin"

@pytest.mark.parametrize("num, result", [(1,11),(2,22), (3,33), (4,44)])
def test_cal(num, result):
    assert 11 * num == result

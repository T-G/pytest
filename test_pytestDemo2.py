import pytest


@pytest.yield_fixture()
def setup():
    print('\nExecuting the test case...')
    yield
    print('\nTest case completed.')


def testmethod1(setup):
    print('\nThis is test method 1')


def testmethod2(setup):
    print('This is test method 2')


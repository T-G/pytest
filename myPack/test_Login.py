import pytest

@pytest.yield_fixture()
def setUp():
    print('\nOpening URl to Login')
    yield
    print('\nClosing browser after Login')

def test_loginByEmail(setUp):
    print('Login in by email test case')


def test_loginByFacebook(setUp):
    print('Login in by facebook test case')
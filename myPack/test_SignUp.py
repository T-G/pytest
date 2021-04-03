import pytest

@pytest.yield_fixture()
def setUp():
    print('\nOpen Url to SignUp')
    yield
    print('\nClose browser after SignUp')


def test_signUpByEmail(setUp):
    print('This Sign up by Email test case')

def test_signUpByFacebook(setUp):
    print('This is Sign up by Facebook test case')
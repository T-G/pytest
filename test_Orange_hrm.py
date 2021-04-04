from selenium import webdriver
import pytest


'''
command to execute this program: pytest -v -s test_Orange_hrm.py
uses: pytest-html package required to generate HTML report
command to execute html default report: pytest -v -s --html=report.html test_Orange_hrm.py
extra parameters can be passed also: pytest -v -s --html=report.html --self-contained-html test_Orange_hrm.py

note: the report will be generated within the project root, if you require to save to 
different path then follow:
pytest -v -s --html=./reports/report.html --self-contained-html test_Orange_hrm.py
'''


class TestOrangeHRM:
    browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

    @pytest.fixture()  # method to execute before any method call
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=self.browser_driver_location)
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_home_page_title(self, setup):
        self.driver.get(r'https://opensource-demo.orangehrmlive.com/')
        assert self.driver.title == 'OrangeHRM123'

    def test_login(self, setup):
        self.driver.get(r'https://opensource-demo.orangehrmlive.com/')
        self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        self.driver.find_element_by_id('btnLogin').click()
        assert self.driver.title == 'OrangeHRM'

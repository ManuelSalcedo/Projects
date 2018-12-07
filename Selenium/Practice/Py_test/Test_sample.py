from selenium import webdriver
import pytest

# https://docs.pytest.org/en/latest/contents.html

# pytest naming: file and functions are test_*.py or *_test.py
#                class are Test*
# Also can use classes
# if so, include slef in def(self)
class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Complete")

    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        
    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test Complete")
    
# Run
# $ pytest -v Test_sample.py
import pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PytestAppiumTests:
    search_words = ('Python', 'abirvalg_abirvalg!@#')

    driver = ''

    def setup_methos(self):
        desired_capabilities = {
            "platformName": "Android",
            "appium:platformVersion": "9",
            "appium:deviceName": "emulator-5554",
            "appium:automationName": "Appium",
            "appium:app": "E:\Gurov_SSD_256\IT\Testing\Automation_08_09_2019/appium_class_tests/app_binaries\org.wikipedia.apk",
        }
        self.driver: WebDriver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",
                                                  desired_capabilities=desired_capabilities)

    @pytest.mark.parametrize('search_query', search_words)
    def pytest_appium_tests(self, search_query):
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'org.wikipedia:id/search_container').click()
        e = self.driver.find_element(By.ID, 'org.wikipedia:id/search_src_text')
        e.clear()
        expected_text = f'\"{search_query}\"'
        e.send_keys(expected_text, Keys.ENTER)
        actual_text = self.driver.find_element(By.ID, 'org.wikipedia:id/page_list_item_title').text
        assert expected_text in actual_text, f'Expected "{expected_text}" to be in {actual_text}'

    def teardown_method(self):
        self.driver.quit()


PytestAppiumTests().setup_methos()

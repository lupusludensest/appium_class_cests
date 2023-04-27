from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Android Emulator",
    "app": "E:\Gurov_SSD_256\IT\Testing\Automation_08_09_2019/appium_class_tests/app_binaries\org.wikipedia.apk",
}

driver: WebDriver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)

driver.implicitly_wait(3)

driver.find_element(By.ID, 'org.wikipedia:id/search_container').click()
e = driver.find_element(By.ID, 'org.wikipedia:id/search_src_text')
e.clear()
expected_text = 'Python'
e.send_keys(expected_text, Keys.ENTER)
actual_text = driver.find_element(By.ID, 'org.wikipedia:id/page_list_item_title').text
assert expected_text in actual_text, f'Expected "{expected_text}" to be in {actual_text}'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)

driver.implicitly_wait(3)

driver.find_element(By.ID, 'org.wikipedia:id/search_container').click()
e = driver.find_element(By.ID, 'org.wikipedia:id/search_src_text')
e.clear()
expected_text = 'No results found'
sent_text = 'abirvalg_abirvalg!@#'
e.send_keys(sent_text, Keys.ENTER)
actual_text = driver.find_element(By.ID, 'org.wikipedia:id/search_empty_text').text
assert expected_text in actual_text, f'Expected "{expected_text}" to be in {actual_text}'
driver.quit()
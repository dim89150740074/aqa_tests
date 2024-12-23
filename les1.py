import time
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pickle

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-cache")
options.add_argument("--incognito")
options.add_argument("--ignore-certificate-errors")
# options.add_argument("--headless=new")
options.page_load_strategy = "eager"
driver = webdriver.Chrome(options)
action = ActionChains(driver)
wait = WebDriverWait(driver, 10, 1)

TARGET_TEXT_LOCATOR = ("xpath", "//div[@class='message']")
BTN_CLICK_LOCATOR = ("xpath", "//button")
# BNT_RIGHT_CLICK_LOCATOR = ("xpath", "//button[@id='rightClickBtn']")
# BTN_CLICK_LOCATOR = ("xpath", "//button[text()='Click Me']")

url = "https://expired.badssl.com/ "

# def get_elem(locator):
#     return driver.find_element(*locator)
#
driver.get(url)
# get_elem(BTN_CLICK_LOCATOR).click()
# assert wait.until(EC.text_to_be_present_in_element(TARGET_TEXT_LOCATOR, "Текст изменен")), "Ошибка"
time.sleep(10)







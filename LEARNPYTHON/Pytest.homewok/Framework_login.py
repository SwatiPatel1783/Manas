import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def open_browser():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")


def test_verify_signin_page():
    open_browser()
    driver.find_element(By.CSS_SELECTOR, "div.nav-line-1-container").click()
    assert driver.title == "Amazon Sign In"
    time.sleep(5)

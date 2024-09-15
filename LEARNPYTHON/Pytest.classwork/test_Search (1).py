import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def open_browser():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")

@pytest.mark.smoke
def test_verify_search_suggestion_page():
    open_browser()
    search = driver.find_element(By.NAME, "search")
    search.click()
    search.send_keys("iPhone 15")

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.btn-lg").click()

    assert driver.title == "Search - iPhone 15"
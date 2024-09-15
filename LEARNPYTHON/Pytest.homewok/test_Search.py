import time

from pip._internal.commands import search
from selenium import webdriver
from selenium.webdriver.common.by import By

def open_browser():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")

def test_verify_search_textbox():
    open_browser()
    search_textbox = driver.find_element(By.ID, "twotabsearchtextbox")
    search_textbox.send_keys("baby shampoo")
    driver.find_element(By.ID,"nav-search-submit-button").click()
    time.sleep(5)

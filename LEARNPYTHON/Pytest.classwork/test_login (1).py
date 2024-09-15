# Common actions can be written inside the single function
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def open_browser():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")


def test_verify_login_page():
    open_browser()
    driver.find_element(By.CSS_SELECTOR, "a[title='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    assert driver.title == "Account Login"
    time.sleep(5)


def test_do_login():
    open_browser()
    driver.find_element(By.CSS_SELECTOR, "a[title='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()

    username = driver.find_element(By.NAME, "email")
    username.click()
    username.send_keys("Shreyans")

    password = driver.find_element(By.NAME, "password")
    password.click()
    password.send_keys("asdf")

    driver.find_element(By.XPATH, "//*[@value='Login']").click()
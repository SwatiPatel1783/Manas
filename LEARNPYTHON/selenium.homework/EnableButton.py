import time
from faulthandler import is_enabled

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.amazon.in")
time.sleep(5)

enable = driver.find_element(By.CSS_SELECTOR, ".nav-search-field").is_enabled()

print(enable)

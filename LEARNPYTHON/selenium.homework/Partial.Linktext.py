import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.amazon.in/")

time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT, "Press Rel").click()

time.sleep(10)




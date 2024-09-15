import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.in")
time.sleep(6)

elements = driver.find_elements(By.TAG_NAME, "a")

for element in elements:
    print(element.text)
    print(element.get_attribute("href"))


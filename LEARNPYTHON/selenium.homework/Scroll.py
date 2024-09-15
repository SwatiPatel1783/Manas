import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.in")
time.sleep(5)

element = driver.find_element(By.LINK_TEXT, "Amazon Global Selling")
time.sleep(5)
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(5)





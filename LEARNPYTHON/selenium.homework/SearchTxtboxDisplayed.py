import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.in")
time.sleep(5)

search_box = driver.find_element(By.ID, "twotabsearchtextbox").is_displayed()
time.sleep(5)

print("display")

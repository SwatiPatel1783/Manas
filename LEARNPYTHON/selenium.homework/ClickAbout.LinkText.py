import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.amazon.in/") #Open amazon website

time.sleep(5)

driver.find_element(By.CLASS_NAME, "nav_a").click() #CLick on about us link using link text

time.sleep(5)

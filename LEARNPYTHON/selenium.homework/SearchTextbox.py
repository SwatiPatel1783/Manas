import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.amazon.in/") #Open amazon website

time.sleep(5)

driver.find_element(By.NAME, "site-search").click() #Click on search textbox


time.sleep(5)

#print("Amazon opened in Edge")

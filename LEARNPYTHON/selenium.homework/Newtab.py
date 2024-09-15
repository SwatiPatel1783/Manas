import time

from selenium import webdriver

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.amazon.in/")
time.sleep(10)

driver.switch_to.new_window("TAB")
time.sleep(5)

driver.get("https://www.costco.ca/")

time.sleep(5)



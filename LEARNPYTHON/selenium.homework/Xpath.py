import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://www.automationpractice.pl/index.php')

categories = driver.find_elements(By.XPATH, "//ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/li/a")

target_category = "T-SHIRTS"
for category in categories:
    if category.text == target_category:
        category.click()
        #time.sleep(5)
        break
    else:
        print(category.text)

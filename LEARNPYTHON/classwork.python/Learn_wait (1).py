import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.instagram.com/")

# driver.implicitly_wait(10)

#Explicit wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.element_to_be_clickable((By.NAME,"username")))

driver.find_element(By.NAME, "username").click()

time.sleep(3)
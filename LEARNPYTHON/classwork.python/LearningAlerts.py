# there are 2 types of alerts (1) browser alert & (2) website alert
# alerts has 3 types (1) toast alert (2) confirmation & (3) Textbox alert
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")

# driver.find_element(By.XPATH, "//*[@onclick='alertbox()']").click()
driver.find_element(By.XPATH, "//*[text()='Alert with OK & Cancel ']").click()
time.sleep(3)

driver.find_element(By.XPATH, "//*[@onclick='confirmbox()']").click()

time.sleep(5)

driver.switch_to.alert.dismiss()

time.sleep(5)
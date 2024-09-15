import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")

driver.switch_to.frame(driver.find_element(By.ID, "singleframe"))
driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").click()

time.sleep(3)
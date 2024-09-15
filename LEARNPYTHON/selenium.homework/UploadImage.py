import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://pinetools.com/merge-images")

driver.find_element(By.NAME, "image1").send_keys("C:\\Users\\swati\\Desktop\\SAI.PNG")

time.sleep(7)

print("Image uploaded successfully")
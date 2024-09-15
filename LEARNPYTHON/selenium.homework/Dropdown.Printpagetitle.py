import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(5)

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.click()
search_box.send_keys("the story collector")

time.sleep(5)
driver.find_element(By.ID,  "nav-search-submit-button").click()

time.sleep(3)
print("Page Title:", driver.title)



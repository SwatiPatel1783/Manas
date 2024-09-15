import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")

# driver.find_element(By.CSS_SELECTOR, "#cart-total").click()
# driver.find_element(By.CSS_SELECTOR,".btn.btn-default.btn-lg").click()
# driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']").click()

list_link = driver.find_elements(By.CSS_SELECTOR, "div[class='col-sm-3'] > ul[class='list-unstyled'] >li > a")

for x in list_link:
    if x.text == "My Account":
        x.click()
        break
    else:
        print(x.text)

time.sleep(4)

# tag that is placed beside < sign or line can be start with tag
# Attribute is like type,name,id,placeholder etc..
# Attribute value (=) is written inside the double quotes
# types of locators: Id, name, linktext, partial linktext, tagname, css selectore & xpath

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")


driver.find_element(By.name, "search").click()
#driver.find_element(By.ID, "cart-total").click()
#driver.find_element(By.LINK_TEXT, "About us").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "About").click()

time.sleep(5)


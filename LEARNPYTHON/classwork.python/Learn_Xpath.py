# xpath stands for the axis path
# xpath has 2 types (1) Absoulate & (2) Relative
# Absolute xpath: it is start from / and html tag(it is a root tag). it is not recommended
#Relative xpath: it is starting from //
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo")

# driver.find_element(By.XPATH ,"/html/body/header/div/div/div[2]/div/input").click() # it is absoulate xpath

# relative xpath syntax:
# Syntax is //tagname[@attrtibute = 'attrtibute value']

# driver.find_element(By.XPATH, "//input[@placeholder='Search']").click()
# driver.find_element(By.XPATH, "//span[@id='cart-total']").click()
# driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

# if you don't want to write the tag name then use the * sign at tagname place
# driver.get("https://tutorialsninja.com/demo/index.php?route=product/category&path=20_27")
# driver.find_element(By.XPATH, "//*[@id='input-sort']").click()


# build the xpath using visible text
# driver.find_element(By.XPATH, "//*[text()='About Us']").click()

#build the xpath using and & or condition
# driver.find_element(By.XPATH, "//*[@title='My Account' and @class='dropdown-toggle']").click()

# driver.find_element(By.XPATH, "//*[@title='My Account' or @class='dropdown-toggle1']").click()

element = driver.find_elements(By.XPATH, "//h4/a")
for x in element:
    getCategory = x.text
    if getCategory == "iPhone":
        x.click()
        break
    else:
        print(getCategory)
        
time.sleep(4)
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")


product_links = driver.find_elements(By.CSS_SELECTOR, "div>h4>a")


for link in product_links:
    if "iPhone" in link.text:
        link.click()
        break
    else:
        print(link.text)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
.........WAIT..........
# Initialize the WebDriver (for example, using Chrome)
driver = webdriver.Chrome()
# Open Instagram
driver.get("https://www.instagram.com/")
# Explicit wait
wait = WebDriverWait(driver, 10)
# Wait until the username field is clickable
username_field = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
# Click the username field
username_field.click()
"""

"""  
.....FRAME.....   
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (for example, using Chrome)
driver = webdriver.Chrome()
# Maximize the browser window
driver.maximize_window()
# Open the target webpage
driver.get("https://demo.automationtesting.in/Frames.html")
# Switch to the frame by its ID
driver.switch_to.frame(driver.find_element(By.ID, "singleframe"))
# Find the input field inside the frame and click it
driver.find_element(By.XPATH, "//input[@type='text']").click()
# Wait for a few seconds (not the best practice; consider using WebDriverWait instead)
time.sleep(3)
# Optional: Close the browser
driver.quit()
"""
#copy = clt f
"""
.....CSS LOCATOR......

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()
# Open the target webpage
driver.get("https://tutorialsninja.com/demo/")
driver.find_element(By.CSS_SELECTOR,".btn.btn-default.btn-lg").click()
time.sleep(4)
# Use WebDriverWait to wait for the element to be clickable
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-default.btn-lg")))
# Click the button
button.click()
# Wait for a few seconds (optional, for demonstration purposes)
time.sleep(4)

# Close the browser (optional)
driver.quit()
"""

"""
driver = webdriver. Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")

# driver.find_element(By.CSS_SELECTOR, "#cart-total").click()|
# driver.find_element(By.CSS_SELECTOR,".btn.btn-defoult.btn-lg").click()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']").click()
time.sleep(4)
"""


"""import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver. Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")

# driver.find_element(By.CSS_SELECTOR, "#cart-total").click()
# driver.find_element(By.CSS_SELECTOR,".btn.btn-default.btn-lg").click()
# driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']").click()

list_link = driver.find_elements(By.CSS_SELECTOR, "div[class='col-sm-3'] > ul[class='list-unstyled' ] >li > a")

for x in list_link:
if x.text == "My Account":
x.click()
break

else:
print(x.text)

time.sleep(4)"""


"""import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")

# Find all the links in the specified section
list_link = driver.find_elements(By.CSS_SELECTOR, "div[class='col-sm-3'] > ul[class='list-unstyled'] > li > a")

# Iterate through the links and click on "My Account" if found
for x in list_link:
    if x.text == "My Account":
        x.click()
        break
    else:
        print(x.text)

# Wait for a while to see the result
time.sleep(4)

# Close the browser
driver.quit()"""



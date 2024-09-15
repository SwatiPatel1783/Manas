from selenium import webdriver


def open_website():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/index.php")

def print_title():
    print(driver.title)
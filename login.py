from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def startBot(username, password, url):

    # Start Chrome with auto WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(url)

    # Wait until GitHub login form loads
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_field"))
    )

    # Enter username
    driver.find_element(By.ID, "login_field").send_keys(username)

    # Enter password
    driver.find_element(By.ID, "password").send_keys(password)

    # Click login button
    driver.find_element(By.NAME, "commit").click()

    # Wait for a moment
    time.sleep(60)

# -----------------------
username = "Sadashiv"
password = "Sadashiv@123"
url = "https://instagram.com/login"#u can also use github login url here

startBot(username, password, url)

  
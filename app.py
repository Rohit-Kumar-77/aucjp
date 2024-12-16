from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Configure ChromeDriver options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-extensions")

# Path to your ChromeDriver executable
# Use 'chromedriver.exe' as the path
service = Service('chromedriver.exe')

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the website
    url = "https://aucjp.com/japan"
    driver.get(url)

    # Optional: Add a wait to let the page load fully
    time.sleep(5)  # Adjust the wait time as needed

    print("Successfully navigated to", url)

    # Select element by class name 'ajrD_on' and click
    try:
        element = driver.find_element(By.CLASS_NAME, 'ajrD_on')
        element.click()
        print("Clicked on the element with class 'ajrD_on'")
    except Exception as e:
        print("Error finding or clicking the element:", e)

finally:
    # Close the browser after some time
    time.sleep(5)  # Adjust the wait time as needed
    driver.quit()

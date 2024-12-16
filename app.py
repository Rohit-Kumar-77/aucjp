from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    # Select all elements by class name 'ajrD' and click each
    try:
        elements = driver.find_elements(By.CLASS_NAME, 'ajrD')
        for index, element in enumerate(elements):
            try:
                element.click()
                print(f"Clicked on element {index + 1} with class 'ajrD'")
            except Exception as e:
                print(f"Error clicking on element {index + 1}: {e}")
    except Exception as e:
        print("Error finding elements with class 'ajrD':", e)

    # Find the element by ID 'aj1_0' and click it using JavaScript
    try:
        element = driver.find_element(By.ID, 'aj1_0')
        driver.execute_script("arguments[0].click();", element)
        print("Clicked on element with ID 'aj1_0' using JavaScript")

        # After clicking the element with ID 'aj1_0', click the element with class 'search_button_export'
        try:
            export_button = driver.find_element(By.CLASS_NAME, 'search_button_export')
            export_button.click()
            print("Clicked on element with class 'search_button_export'")

            # After clicking 'search_button_export', click the 'my_bids' login button
            # Wait for the element with class 'my_bids' to be clickable
            try:
                login_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'my_bids'))
                )
                login_button.click()
                time.sleep(2000)
                print("Clicked on login button with class 'my_bids'")
            except Exception as e:
                print("Error finding or clicking the login button:", e)

        except Exception as e:
            print("Error finding or clicking the export button:", e)
    except Exception as e:
        print("Error finding or interacting with element 'aj1_0':", e)

finally:
    # Keep the browser open after script completion
    print("Script execution completed. Browser will remain open.")

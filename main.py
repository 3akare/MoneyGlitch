from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import time
import os

# Load env variables
load_dotenv()

# Corrected Chrome profile path
chrome_profile_path = str(os.getenv("CHROME_PROFILE_PATH"))
options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={chrome_profile_path}")
options.add_argument("--profile-directory=Default")  # Change if needed
# options.add_argument("--headless")  # Keep this commented for debugging

# Start Chrome with your existing profile
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the website (should be logged in)
driver.get(str(os.getenv("WEB_URL")))
time.sleep(20)  # Wait for page load

while True:
    try:
        print("Looking for button...")
        button = driver.find_element(By.ID, "playButton")  

        if button:
            print("Button found! Clicking...")
            button.click()
            print("Video started... Waiting 40 seconds")
            time.sleep(60)

            # Refresh the page
            driver.refresh()
            print("Page refreshed. Waiting 20 seconds before next loop...")
            time.sleep(20)

        else:
            print("Button not found!")

    except Exception as e:
        print(f"Error: {e}")
        break  # Exit on error

# Cleanup
driver.quit()

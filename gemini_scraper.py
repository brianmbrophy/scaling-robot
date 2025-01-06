import time
import csv
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

# Logging setup
logging.basicConfig(
    filename="gemini_scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def initialize_driver():
    """Initialize the undetected ChromeDriver."""
    try:
        options = uc.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        driver = uc.Chrome(options=options)
        logging.info("Initialized undetected ChromeDriver.")
        return driver
    except Exception as e:
        logging.error(f"Error initializing driver: {e}")
        raise

def scroll_and_collect_data(driver, writer):
    """Scroll and collect Gemini activity details."""
    activity_data = set()  # Use a set to avoid duplicate entries
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)  # Adjust if necessary for slower loading

        # Iterate through each c-wiz element
        c_wiz_elements = driver.find_elements(By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > div.jkOv3d > c-wiz > c-wiz > div > div:nth-child(1) > c-wiz")
        logging.info(f"Found {len(c_wiz_elements)} c-wiz elements.")
        for index, c_wiz in enumerate(c_wiz_elements):
            try:
                button = c_wiz.find_element(By.CSS_SELECTOR, "div > div > div.gWevEe > div.uUy2re > div.wlgrwd > div > a")
                driver.execute_script("arguments[0].scrollIntoView(true);", button)
                time.sleep(1)  # Allow time for scrolling

                # Ensure the button is visible and clickable
                WebDriverWait(driver, 10).until(
                    EC.visibility_of(button)
                )
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(button)
                )

                # Click the button using JavaScript to avoid interception
                driver.execute_script("arguments[0].click();", button)

                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".KTW5Zd.pFTsBb"))
                )

                # Extract the visible text of the details section
                details_content = driver.find_element(By.CSS_SELECTOR, ".KTW5Zd.pFTsBb").text.strip()
                if details_content not in activity_data:
                    activity_data.add(details_content)  # Add to set to avoid duplicates
                    logging.info(f"Collected data at index {index}: {details_content[:50]}...")
                    writer.writerow({"content": details_content})  # Write to CSV incrementally

                # Navigate back to the main list
                driver.back()
                time.sleep(2)  # Allow time for the page to load

            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException) as e:
                logging.warning(f"Error accessing activity details at index {index}: {e}")
                continue

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            logging.info("Reached the bottom of the page.")
            break
        last_height = new_height

    return list(activity_data)  # Convert set to list before returning

def save_to_csv(data):
    """Save collected data to a CSV file."""
    try:
        with open("/Users/brianbrophy/Lia/data/gemini_chat_history.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["content"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for content in data:
                writer.writerow({"content": content})
        logging.info("Data saved to gemini_chat_history.csv.")
    except Exception as e:
        logging.error(f"Error saving data to CSV: {e}")
        raise

def main():
    """Main function to scrape Google Gemini chat history."""
    driver = None
    try:
        driver = initialize_driver()
        driver.get("https://myactivity.google.com/product/gemini")
        logging.info("Navigated to Google Gemini My Activity page.")

        input("Please log in manually, then press Enter to continue...")

        logging.info("Scrolling and collecting Gemini activity data...")

        with open("/Users/brianbrophy/Lia/data/gemini_chat_history.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["content"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            gemini_data = scroll_and_collect_data(driver, writer)

        logging.info("Data collection complete.")

    except Exception as e:
        logging.critical(f"Critical error in main function: {e}")
    finally:
        if driver:
            driver.quit()
            logging.info("Driver closed.")

if __name__ == "__main__":
    main()
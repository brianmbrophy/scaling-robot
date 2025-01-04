# scaling-robot
oogle Gemini Chat History Scraper

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-success.svg)](https://www.selenium.dev/)

This script automates the extraction of your chat history from Google Gemini (via Google My Activity) and saves it to a CSV file. Google doesn't provide an official export for this data, and this script provides a way to access and archive your conversations.

## Features

* **Automates Navigation:** Logs into your Google account (manual login required).
* **Dynamic Content Loading:** Scrolls through the page to load all chat history.
* **"Details" Expansion:** Automatically clicks the "Details" button for each chat entry to reveal the full conversation.
* **Data Extraction:** Extracts the text content of each conversation.
* **CSV Output:** Saves the extracted data to a `gemini_chat_history.csv` file in the script's directory.

## Setup

1. **Prerequisites:**
   - [Python 3.8+](https://www.python.org/downloads/) installed on your system.
   - [Google Chrome](https://www.google.com/chrome/) installed on your system.

2. **Install Python Libraries:**
   Open your terminal or command prompt and run:
   ```bash
   pip install selenium webdriver-manager
Use code with caution.
Markdown
Usage
Save the Script: Save the provided Python script (the one we finalized) as a .py file (e.g., gemini_scraper.py).

Run the Script: Open your terminal or command prompt, navigate to the directory where you saved the script, and run it:

python gemini_scraper.py
Use code with caution.
Bash
Manual Login: The script will open a Chrome browser and navigate to the Google My Activity Gemini page. You will need to manually log in to your Google account when prompted in the terminal. After logging in, press Enter in the terminal to continue the script.

Data Extraction: The script will automatically scroll, click, and extract your chat history.

Output File: Once the script finishes, a file named gemini_chat_history.csv will be created in the same directory as the script. This file contains your extracted chat history.

Important Considerations
Personal Data: This script extracts your personal Google Gemini chat history. The extracted data is saved locally on your computer. Handle this file with care and be mindful of its privacy.

Website Changes: Google may change the structure of their My Activity page at any time. This could cause the script to stop working, and it may require updates to the CSS selectors or logic.

ChromeDriver Compatibility: Ensure that the version of ChromeDriver installed by webdriver-manager is compatible with your installed version of Google Chrome. If you encounter issues, you may need to manually manage your ChromeDriver.

Rate Limiting: While this script includes pauses, excessive use might be detected by Google. Use responsibly.

Troubleshooting
ElementNotInteractableException or ElementClickInterceptedException: This might occur if elements are loading slowly or being covered by other elements. You can try increasing the time.sleep() values in the script.

NoSuchElementException: If this error occurs, it means the script couldn't find an element using the specified CSS selector (.WFTFcf, div.KTW5Zd.pFTsBb). The website structure might have changed, and you'll need to inspect the page source and update the selectors.

Script Freezes: If the script seems to stop, check the terminal for any error messages.

Disclaimer
This script is provided as-is for informational and personal use. The author is not responsible for any issues arising from its use.

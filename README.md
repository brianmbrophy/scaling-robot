Markdown
## Google Gemini Chat History Scraper

This script automates the extraction of your chat history from Google Gemini (via Google My Activity) and saves it to a CSV file.

### Features
- Automates Navigation: Logs into your Google account (manual login required).
- Dynamic Content Loading: Scrolls through the page to load all chat history.
- "Details" Expansion: Automatically clicks the "Details" button for each chat entry to reveal the full conversation.
- Data Extraction: Extracts the text content of each conversation.
- CSV Output: Saves the extracted data to a `gemini_chat_history.csv` file in the script's directory.

### Setup
1. **Prerequisites:**
   - [Python 3.8+](https://www.python.org/downloads/) installed on your system.
   - [Google Chrome](https://www.google.com/chrome/) installed on your system.

2. **Install Python Libraries:**
   Open your terminal or command prompt and run:
   ```bash
   pip install selenium undetected-chromedriver
Usage
Save the provided Python script as gemini_scraper.py.
Run the script:
python gemini_scraper.py
Manually log in to your Google account when prompted.
The script will automatically scroll, click, and extract your chat history.
Important Considerations
Personal Data: This script extracts your personal Google Gemini chat history. Handle the extracted data with care and be mindful of its privacy.
Website Changes: Google may change the structure of their My Activity page at any time. This could cause the script to stop working, requiring updates to the CSS selectors or logic.
Rate Limiting: Use the script responsibly to avoid excessive usage detection by Google.
Troubleshooting
If you encounter issues, try increasing the time.sleep() values in the script.
Ensure the version of ChromeDriver installed by undetected-chromedriver is compatible with your installed version of Google Chrome.
Disclaimer
This script is provided as-is for informational and personal use. The author is not responsible for any issues arising from its use.

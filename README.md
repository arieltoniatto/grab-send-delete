
# Grab, send and delete

This is a Python script that allows you to retrieve Google Chrome cookies, including the current user's username and external IP address. The script uses the Selenium library to control the Chrome browser and interact with it programmatically.

## Prerequisites

Before using the script, you need to have the following prerequisites installed:

1. Python 3.x
2. Google Chrome browser
3. ChromeDriver (compatible with your Chrome version) installed and accessible from the system's PATH
4. Required Python packages: `selenium`, `requests`

You can install the necessary Python packages using pip:

```
pip install selenium requests chromedriver_autoinstaller
```

## How to Use

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

```
python chrome_cookies_retrieval.py
```

4. The script will open the Chrome browser, load a blank page, retrieve the cookies, and then display them along with the current user's username and external IP address.

5. After displaying the cookies, the script will save them, along with the metadata, to a JSON file named `chrome_cookies_with_metadata.json`.

6. If you specify a URL in the script (variable `url`), it will send the JSON file to that URL via an HTTP POST request using the `requests` library. Replace `'https://example.com/upload'` with your desired URL.

7. Upon successful file upload (HTTP status code 200), the script will self-delete the JSON file and then self-delete the script file.

## Important Note

- The self-deletion feature is potentially dangerous and irreversible. Use it with caution and only in specific scenarios where necessary.
- Before using the self-deletion feature, ensure you have thoroughly tested the script and verified its behavior.
```

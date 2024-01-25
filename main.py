import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Install the necessary libraries: Selenium and ChromeDriver
# pip install selenium
# Download ChromeDriver: https://sites.google.com/a/chromium.org/chromedriver/downloads

# Set up the Chrome driver
brave_options = webdriver.ChromeOptions()
brave_options.binary_location = "C:\\Users\\Admin\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" # Update with your path

    # Set up the Selenium WebDriver
driver = webdriver.Chrome(options=brave_options)


# Navigate to the Instagram post
post_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
driver.get(post_url)

# Scroll down to load all the comments
SCROLL_PAUSE_TIME = 10

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with the last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Extract the comments
    comments = driver.find_elements(By.CSS_SELECTOR, "div.C4VMK > span")
    for comment in comments:
        print(comment.text)

# Close the browser window
driver.quit()
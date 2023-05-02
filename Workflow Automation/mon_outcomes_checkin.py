from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "chromedriver.exe"
url = "https://docs.google.com/forms/d/e/1FAIpQLScqkWWKJoFIPoGU2zhccrnG7DDltr1YgIUDus_W7z7kA-9NGw/viewform"

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)
driver.get(url)

# Wait for the user to close the browser manually
input("Press Enter to close the browser...")

driver.close()

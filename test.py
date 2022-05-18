from selenium import webdriver
import os 

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.getenv('GOOGLE_CHROME_BIN',None)
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=os.getenv('CHROMEDRIVER_PATH',None), chrome_options=chrome_options)

driver.get('https://www.google.com.tw/')

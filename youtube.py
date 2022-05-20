from selenium import webdriver
import os 

def youtube():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.getenv('GOOGLE_CHROME_BIN',None)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=os.getenv('CHROMEDRIVER_PATH',None), chrome_options=chrome_options)
    driver.get('https://www.youtube.com/c/NaNaShuoMeiGu/videos')
    total = []
    title = driver.find_element_by_id('video-title').get_attribute('title')
    url_video = driver.find_element_by_id('video-title').get_attribute('href')
    total.append(f'{title}: {url_video}' + "\n")
    driver.get('https://www.youtube.com/c/%E9%98%B3%E5%85%89%E8%B4%A2%E7%BB%8F/videos')
    title = driver.find_element_by_id('video-title').get_attribute('title')
    url_video = driver.find_element_by_id('video-title').get_attribute('href')
    total.append(f'{title}: {url_video}' + "\n")
    driver.close()
    return str(total)




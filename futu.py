from selenium import webdriver
import os 

def futu_news():  
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.getenv('GOOGLE_CHROME_BIN',None)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=os.getenv('CHROMEDRIVER_PATH',None), chrome_options=chrome_options)
    driver.get('https://news.futunn.com/hk/main?lang=zh-hk')
    titles = driver.find_elements_by_class_name('news-title')[:10]
    news = []
    for i, c in enumerate(titles):
        url = driver.find_element_by_xpath(f'//*[@id="news-list-container"]/li[{i+1}]/a').get_attribute('href')
        news.append(f'{c.text} {url}')
    driver.close()
    return str(news)


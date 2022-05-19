from selenium import webdriver
import os 

def futu_news():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://news.futunn.com/hk/main?lang=zh-hk')
    driver.maximize_window()
    titles = driver.find_elements_by_class_name('news-title')[:10]
    news = []
    for i, c in enumerate(titles):
        url = driver.find_element_by_xpath(f'//*[@id="news-list-container"]/li[{i+1}]/a').get_attribute('href')
        news.append(f'{c.text} {url}')
    driver.close()
    return str(news)

def futu_news_us():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://news.futunn.com/hk/main?lang=en-US')
    driver.maximize_window()
    titles = driver.find_elements_by_class_name('news-title')[:10]
    news = []
    for i, c in enumerate(titles):
        url = driver.find_element_by_xpath(f'//*[@id="news-list-container"]/li[{i+1}]/a').get_attribute('href')
        news.append(f'{c.text} {url}')
    driver.close()
    return str(news)
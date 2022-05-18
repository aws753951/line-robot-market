import requests
from bs4 import BeautifulSoup

def gdp_index():
    url = 'https://www.bea.gov/data/gdp/gross-domestic-product'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    r = requests.get(url, headers=headers)
    basic_url = 'https://www.bea.gov/'
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'lxml')
        target = soup.find('li', class_='list-group-item').find('a').get('href')
        target_url = basic_url + target
        return target_url

def gdp_index_inv():
    url = 'https://www.investing.com/economic-calendar/gdp-375'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'lxml')
        all_ = soup.find_all(attrs={'event_attr_id':'375'})
        data = []
        for i in all_:
            date_to_release = i.find_next('td')
            value = date_to_release.find_next(class_='noWrap')
            data.append(f'{date_to_release.string}: {value.string}')
        return str(data)





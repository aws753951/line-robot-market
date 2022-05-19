import requests
from bs4 import BeautifulSoup

def cpi_index_inv():
    url = 'https://www.investing.com/economic-calendar/cpi-733'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'lxml')
        all_ = soup.find_all(attrs={'event_attr_id':'733'})
        data = []
        for i in all_:
            date_to_release = i.find_next('td')
            value = date_to_release.find_next('span')
            data.append(f'{date_to_release.string}: {value.string}')
        return str(data)

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

def sales_index_inv():
    url = 'https://hk.investing.com/economic-calendar/retail-sales-256'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'lxml')
        all_ = soup.find_all(attrs={'event_attr_id':'256'})
        data = []
        for i in all_:
            date_to_release = i.find_next('td')
            value = date_to_release.find_next(class_='noWrap')
            data.append(f'{date_to_release.string}: {value.string}')
        return str(data)

def sales_index():
    url = 'https://www.census.gov/retail/index.html'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    r = requests.get(url, headers=headers)
    basic_url = 'https://www.census.gov/'
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'lxml')
        target = soup.find('li', attrs={'style':'margin-top: -8px;'}).find_all('a')[1].get('href')
        target_url = basic_url + target
        return target_url



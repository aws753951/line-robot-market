import requests
from bs4 import BeautifulSoup

def cpi_index():
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

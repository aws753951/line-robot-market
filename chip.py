import requests
from bs4 import BeautifulSoup
import re
import pprint

def chip():
    url = 'https://dataroma.com/m/home.php'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'lxml')
        all_ = soup.find(id='port_body').find_all('a')
        chiplists = []
        names = []
        for list_ in all_:
            name1 = re.search(r'(.*).+Updated', list_.text).group(1).lower()   
            name2 = name1.replace('-', '').replace(',', ' ').replace('&', ' ').split()
            name = ''
            for i in name2:
                name += i + ' '
            href = re.search(r'=(.+)', list_.get('href')).group(1)
            url = f'https://dataroma.com/m/m_activity.php?m={href}&typ=a'
            chiplists.append((name, url))

      
   
        return chiplists



# print([chip()[i][1] for i, c in enumerate(chip()) if 'warren  buffet' in c[0]][0])


# for i, c in enumerate(chip()):
#     if 'sss' in c[0]:
#         print(chip()[i][1])


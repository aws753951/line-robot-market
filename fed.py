import requests
import re

def fed_news():
    url = 'https://api.queryly.com/cnbc/json.aspx?queryly_key=31a35d40a9a64ab3&query=fed&endindex=0&batchsize=10&callback=&showfaceted=false&timezoneoffset=-480&facetedfields=formats&facetedkey=formats%7C&facetedvalue=!Press%20Release%7C&needtoptickers=1&additionalindexes=4cd6f71fbf22424d,937d600b0d0d4e23,3bfbe40caee7443e,626fdfcd96444f28'
    r = requests.get(url)
    total = []
    if r.status_code == requests.codes.ok:
        data = r.json()
        news = data['results']
        for new in news:
            title = new['cn:title']
            url_new = new['cn:liveURL']
            total.append((title, url_new))

    return str(total)




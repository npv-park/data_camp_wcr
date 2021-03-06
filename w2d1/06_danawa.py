import requests
from bs4 import BeautifulSoup as bs

with requests.Session() as s:
    s.headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    login = s.post('https://auth.danawa.com/login', data={
        'id': '',
        'password': '',
    })
    html = s.get('http://cws.danawa.com/point/index.php')
    html.encoding = 'euc-kr'
    print(html.text)

import requests
import http.cookiejar as cookielib
import json
from .local import pocker_access_token, pocket_consumer_key


session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
session.cookies.load(ignore_discard=True)


def get_json(pid):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Host': 'zhuanlan.zhihu.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36',
    }
    url = 'https://zhuanlan.zhihu.com/api/posts/{pid}'.format(pid=pid)
    return json.loads(session.get(url, headers=headers).text)


def get_data(json, pid):
    data = dict()
    data['url'] = 'https://zhuanlan.zhihu.com/api/posts/{pid}'.format(pid=pid)
    data['title'] = json['title']
    return data


def save_pocket(pid):
    data = get_data(get_json(pid), pid)
    data['consumer_key'] = pocket_consumer_key
    data['access_token'] = pocker_access_token
    pocket_add = requests.post('https://getpocket.com/v3/add', data=data)
    print(pocket_add.status_code)


while True:
    inp = input('pid or q \n')
    if inp == 'q':
        break
    save_pocket(inp)




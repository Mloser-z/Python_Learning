# 储存为JSON
import requests
import json
from bs4 import BeautifulSoup

if __name__ == '__main__':
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    url = 'http://seputu.com/'
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers)
    print(r.text)

    soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
    content = []
    for mulu in soup.find_all(class_='mulu'):
        h2 = mulu.find('h2')
        if h2 is not None:
            h2_title = h2.string  # 获取标题
            title_list = []
            for a in mulu.find(class_='box').find_all('a'):
                href = a.get('href')
                box_title = a.get('title')
                title_list.append({'href': href, 'box_title': box_title})
            content.append({'title': h2_title, 'content': title_list})
    with open('qiye.json', 'w') as fp:
        json.dump(content, fp=fp, indent=4)
    with open('qiye.json', 'r') as fr:
        for title in json.load(fr):
            print(title)

# GET
import requests


if __name__ == '__main__':
    r = requests.get('https://www.baidu.com')
    print(r.content)

# requests.get()
# requests.delete()
# requests.head()
# requests.options()
# requests.put()

from lxml import etree
import requests


def schedule(block_num, block_size, total_size):
    """''
    block_num: 已下载的数据块
    block_size: 数据块的大小
    total_size: 远程文件的大小
    """
    per = 100.0 * block_num * block_size / total_size
    if per > 100:
        per = 100
    print('当前下载进度：%d' % per)


def get_picture(url, p_path):
    p_user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Window NT)'
    p_headers = {'User-Agent': p_user_agent}
    rp = requests.get(url, headers=p_headers)
    with open(p_path, 'wb') as f:
        for chunk in rp.iter_content(chunk_size=128):
            f.write(chunk)


if __name__ == '__main__':
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Window NT)'
    headers = {'User-Agent': user_agent}
    r = requests.get('https://www.ivsky.com/tupian/bianxingjingang_v622/', headers=headers)
    # 使用lxml解析网页
    html = etree.HTML(r.text)
    img_urls = html.xpath('.//img/@src')  # 找到所有的img
    i = 0
    for img_url in img_urls:
        img_url = 'https:' + img_url
        print(img_url)
        path = 'learning' + str(i) + '.jpg'
        get_picture(img_url, path)
        i += 1

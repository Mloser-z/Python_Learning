# coding utf-8
import requests
from bs4 import BeautifulSoup
import pymysql


def download_html(url):
    if url is None:
        return None
    user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Window NT)'
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        r.encoding = 'utf-8'
        return r.text
    else:
        print("Download failed")
        return None


def parser_url(text):
    soup = BeautifulSoup(text, 'lxml')
    video_names = []
    video_datas = []
    video_collections = []
    # video_points = []

    for title in soup.find_all(class_='title'):
        video_names.append(title.string)
    for detail in soup.find_all(class_='detail'):
        for video_data in detail.find_all(class_='data-box'):
            video_datas.append(video_data.text.strip())
    # for video_point in soup.find_all(class_='pts'):
    #    video_points.append(video_point.div.string)
    for i in range(0, len(video_datas), 3):
        # video_collections.append([video_names[int(i / 3)], video_datas[i], video_datas[i + 1], video_datas[i + 2],
        #                          video_points[int(i / 3)]])
        video_collections.append([video_names[int(i / 3)], video_datas[i], video_datas[i + 1], video_datas[i + 2]])

    return video_collections


def stored_data(video_datas):
    try:
        db = pymysql.connect(host=input("host:"), user=input("user:"), port=613, password=input("password:"), database=input("database:"), charset='utf8mb4')
    except Exception:
        print("Mysql connect failed")
        return
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS BILIBILI_RANK")
    sql_create_table = """CREATE TABLE BILIBILI_RANK (
            VIDEO_NAME      CHAR(100)    NOT NULL,
            UP_NAME         CHAR(20)    NOT NULL,
            VIEW_NUMBER     CHAR(10)    NOT NULL,
            PLAY_NUMBER     CHAR(20)    NOT NULL
            )"""
    sql_change_charset = """ALTER TABLE BILIBILI_RANK CONVERT TO CHARACTER SET utf8mb4"""
    cursor.execute(sql_create_table)
    cursor.execute(sql_change_charset)
    db.commit()
    for video_data in video_datas:
        print(video_data[0], video_data[1], video_data[2], video_data[3])
        try:
            sql_insert_data = 'INSERT INTO BILIBILI_RANK(VIDEO_NAME, UP_NAME, VIEW_NUMBER, PLAY_NUMBER) VALUES\
                          (%s, %s, %s, %s)'
            var = (video_data[0], video_data[1], video_data[2], video_data[3])
            cursor.execute(sql_insert_data, var)
            db.commit()

        except Exception as e:
            sql_insert_data = 'INSERT INTO BILIBILI_RANK(VIDEO_NAME, UP_NAME, VIEW_NUMBER, PLAY_NUMBER) VALUES\
                                      (%s, %s, %s, %s)'
            var = ("DataError", video_data[1], video_data[2], video_data[3])
            cursor.execute(sql_insert_data, var)
            db.commit()

    db.close()


if __name__ == '__main__':
    url_text = download_html('https://www.bilibili.com/v/popular/rank/all')
    videos = parser_url(url_text)
    stored_data(videos)

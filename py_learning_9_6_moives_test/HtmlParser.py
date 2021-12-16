# coding utf-8
import json
import re


class HtmlParser:
    def parser_url(self, response):
        pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
        urls = pattern.findall(str(response))
        if urls is not None:
            # 将urls进行去重
            return list(set(urls))
        else:
            return None

    def parser_json(self, page_url, response):
        # 将"="和";"之间的内容提取出来
        pattern = re.compile(r'=(.*?);')
        result = pattern.findall(response)[0]
        if result is not None:
            # json模块加载字符串
            value = json.loads(result)
            try:
                is_release = value.get('value').get('isRelease')
            except Exception as e:
                print(e)
                return None
            if is_release:
                if value.get('value').get('hotValue') is None:
                    return self._parser_release(page_url, value)
                else:
                    return self._parser_no_release(page_url, value, is_release=2)
            else:
                return self._parser_no_release(page_url, value)

    def _parser_release(self, page_url, value):
        """
        解析已经上映的影片
        :param page_url:电影链接
        :param value: json
        :return:
        """
        try:
            is_release = 1
            movie_rating = value.get('value').get('movieRating')
            box_office = value.get('value').get('boxOffice')
            movie_title = value.get('value').get('movieTitle')
            r_picture_final = movie_rating.get('RPictureFinal')
            r_story_final = movie_rating.get('RStoryFinal')
            r_directory_final = movie_rating.get('RDirectoryFinal')
            r_other_final = movie_rating.get('ROtherFinal')
            rating_final = movie_rating.get('RatingFinal')

            movie_id = movie_rating.get('MovieId')
            user_count = movie_rating.get('UserCount')
            attitude_count = movie_rating.get('AttitudeCount')
            total_box_office = box_office.get('TotalBoxOffice')
            total_box_office_unit = box_office.get('TotalBoxOfficeUnit')
            today_box_office = box_office.get('TodayBoxOffice')
            today_box_office_unit = box_office.get('TodayBoxOfficeUnit')

            show_days = box_office.get('ShowDays')
            try:
                rank = box_office.get('Rank')
            except Exception as e:
                rank = 0
            # return
            return [movie_id, movie_title, rating_final, r_other_final,
                    r_picture_final, r_directory_final, r_story_final, user_count,
                    attitude_count, total_box_office + total_box_office_unit,
                    today_box_office + today_box_office_unit,
                    rank, show_days, is_release]
        except Exception as e:
            print(e, page_url, value)
            return None

    def _parser_no_release(self, page_url, value, is_release=0):
        """
        解析未上映电影信息
        :param page_url:
        :param value:
        :param is_release:
        :return:
        """
        try:
            movie_rating = value.get('value').get('movieRating')
            movie_title = value.get('value').get('movieTitle')
            r_picture_final = movie_rating.get('RPictureFinal')
            r_story_final = movie_rating.get('RStoryFinal')
            r_directory_final = movie_rating.get('RDirectoryFinal')
            r_other_final = movie_rating.get('ROtherFinal')
            rating_final = movie_rating.get('RatingFinal')

            movie_id = movie_rating.get('MovieId')
            user_count = movie_rating.get('UserCount')
            attitude_count = movie_rating.get('AttitudeCount')
            try:
                rank = value.get('value').get('hotValue').get('Ranking')
            except Exception as e:
                rank = 0
            return [movie_id, movie_title, rating_final, r_other_final,
                    r_picture_final, r_directory_final, r_story_final,
                    user_count, attitude_count, u'无', u'无', rank, 0, is_release]
        except Exception as e:
            print(e, page_url, value)
            return None

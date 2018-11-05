# -*- coding: utf-8 -*-
import scrapy,json
from zhihuusers.items import UsersItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']

    user_url = 'https://www.zhihu.com/api/v4/members/{url_token}?include={user_query}'
    user_query = '%20voteup_count,thanked_count,follower_count,following_count,answer_count,articles_count,' \
                  'pins_count,question_count,favorite_count,favorited_count,logs_count,marked_answers_count,' \
                  'marked_answers_text,account_status,is_active,is_force_renamed,description,' \
                  'badge[?(type=best_answerer)].topics'
    start_user = 'zhang-jia-wei'

    following_url = 'https://www.zhihu.com/api/v4/members/{url_token}/followees?include=data%5B*' \
                    '%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Ci' \
                    's_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'

    def start_requests(self):
        yield scrapy.Request(url=self.user_url.format(url_token=self.start_user, user_query=self.user_query), callback=self.parse_user)

    def parse_user(self, response):
        response = json.loads(response.text)
        item = UsersItem()
        for field in item.fields:
            if field in response.keys():
                item[field] = response.get(field)

        if item['follower_count']>20000:
            yield scrapy.Request(url=self.following_url.format(url_token = item['url_token']),callback=self.parse_following)

        yield item


    def parse_following(self,response):
        response = json.loads(response.text)
        if 'data' in response.keys():
            for fans in response.get('data'):
                yield scrapy.Request(url=self.user_url.format(url_token=fans['url_token'],user_query=self.user_query),
                                     callback=self.parse_user)

        if 'paging' in response.keys():
            if not response.get('paging').get('is_end'):
                nextpage = response.get('paging').get('next')
                yield scrapy.Request(url=nextpage,callback=self.parse)







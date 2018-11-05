# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UsersItem(scrapy.Item):
    # define the fields for your item here like:
    #基本信息
    name = scrapy.Field()
    url = scrapy.Field() #知乎主页
    url_token = scrapy.Field()
    headline = scrapy.Field() #一句话简介
    is_org = scrapy.Field() #机构账号

    #个人成就
    following_count = scrapy.Field() #关注
    follower_count = scrapy.Field() #粉丝
    voteup_count = scrapy.Field() #赞同
    thanked_count = scrapy.Field() #感谢
    favorited_count = scrapy.Field() #被收藏
    logs_count = scrapy.Field() #公共编辑
    marked_answers_count = scrapy.Field() #收录内容
    badge = scrapy.Field() #话题认证

    #个人行为
    answer_count = scrapy.Field() #回答数
    articles_count = scrapy.Field() #文章数
    pins_count = scrapy.Field() #想法数
    question_count = scrapy.Field() #提问数
    favorite_count = scrapy.Field() #收藏数


    #账户状态
    account_status = scrapy.Field()
    is_active = scrapy.Field()
    is_force_renamed = scrapy.Field()



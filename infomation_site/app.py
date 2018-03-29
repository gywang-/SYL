#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 一个资讯网站

from flask import Flask
import json, os

app = Flask(__name__)

class article(object):
    def __init__(self):
        self.file_dir = os.getcwd() +'/files'
        self.filename = os.listdir(self.file_dir)
#     获取json中的内容 
    def get_json_content(self):
        content_dict = {}
        for i in self.filename:
            fle = self.file_dir + '/' + i
            with open(fle) as f:
                content_dict[i] = json.load(f)
        return content_dict
# 主页文章名称        
    def get_title(self):
        a = self.get_json_content()
        return [ item['title'] for item in a.values() ]


@app.route('/')  
def index():
    index_html = article()
    contents = index_html.get_title()
    return [contents[x] for x in range(len(contents))]

if __name__ == '__main__':
    app.run()

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

    def get_json_content(self):
        content_dict = {}
        for i in self.filename:
            file = self.file_dir + '/' + i
            with open(file,'r') as f:
                ff = f.read()
                bb = json.dumps(ff)
                content_dict[i] = json.loads(bb)
        return content_dict
        


@app.route('/')  
def index():
    index_html = article()
    contents = index_html.get_json_content()
    return str(contents)

if __name__ == '__main__':
    app.run()

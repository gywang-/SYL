#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 一个资讯网站

from flask import Flask, render_template, abort, redirect, url_for
import json, os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

class article(object):
    def __init__(self):
        self.file_dir = os.getcwd() + '/..'  +  '/files'
        self.filename = os.listdir(self.file_dir)
#     获取json中的内容 
    def get_json_content(self):
        content_dict = {}
        for i in self.filename:
            fle = self.file_dir + '/' + i
            with open(fle) as f:
                content_dict[i[:-5]] = json.load(f)
        return content_dict
# 主页文章
    def get_title(self):
        a = self.get_json_content()
        return [ item['title'] for item in a.values() ]

#file = article()

@app.route('/')
def index():
    index_html = article()
    return render_template('index.html',titles = index_html.get_title())

@app.route('/files/<filename>')
def file(filename):
    files = article()
    key_list = files.get_json_content()
    if filename not in key_list.keys():
        abort(404)
    else:
        return render_template('file.html',file = files.get_json_content()[filename])
    
#        a = files.get_json_content()
#        for key, value in a.items():
#            b = a[filename]
#            return render_template('file.html', url_name = key, value_name = value['tit    le'])

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()

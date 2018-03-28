import os, json

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
                content_dict[file] = json.loads(ff)
        print(content_dict)


test = article()

test.get_json_content()

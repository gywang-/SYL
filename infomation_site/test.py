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
                bb = json.dumps(ff)
#                print(type(bb))
                content_dict[i] = json.loads(bb)
#        print(content_dict)
#        print(type(content_dict))
        return content_dict


test = article()

a = test.get_json_content()
print(a)

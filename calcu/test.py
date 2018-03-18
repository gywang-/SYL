#!/usr/bin/env python3

filename = '/home/shiyanlou/test.cfg'

with open(filename,'r') as file:
    config_dict = {}
    for i in file.readlines():
       a = i.strip()
       config_dict.setdefault(a.split(' = ')[0],a.split(' = ')[1])
       
    print(config_dict)
    print(type(config_dict)) 


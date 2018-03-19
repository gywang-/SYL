#!/usr/bin/env python3
import sys
import json

# read config info

class config_info(object):
    def __init__(self,social_file,deployee_file,wage_file):
    #def config_info(social_file,deployee_file,wage_file):
    # social_file 社保比例配置文件
    # deployee_file 员工工资数据文件，文件中包含两列员工号及税前工资金额，例：101:3500 
    # wage_file 计算后的工资详细信息输出
       # global wage
        global social_tax
        global JSL
        global JSH
        global deployee
        # 将社保配置文件读取并存储到dict中
        with open(social_file,'r') as socials:
            social = {}
            for i in socials.readlines():
                a = i.strip()
                social.setdefault(a.split(' = ')[0],a.split(' = ')[1])
        # 将员工ID及工资分隔并存到dict中
        with open(deployee_file,'r') as deployees:
            deployee = {}
            for i in deployees.readlines():
                a = i.strip()
                deployee.setdefault(a.split(',')[0],float(a.split(',')[1]))
        # 设置calc_course要用到的变量
        social_tax = float(social['YangLao']) + float(social['YiLiao']) + float(social['ShiYe']) + float(social['GongShang']) + float(social['ShengYu']) + float(social['GongJiJin'])
        JSL = float(social['JiShuL'])
        JSH = float(social['JiShuH'])
        print(deployee)
    # 工资计算过程
class calc_course(object):
    def __init__(self,deployee,JSL,JSH,social_tax):
    # 社保应缴纳金额
        if wage <= JSL:
            social_sum = format (JSL * social_tax,'.2f')
        elif wage > JSL and wage < JSH:
            social_sum = format(wage * social_tax,'.2f')
        else:
            social_sum = format(JSH * social_tax,'.2f')
        print(social_sum)

    
if __name__ == '__main__':
    args = sys.argv[1:]
#try:
    social_index = args[int(args.index('-c')) + 1]
    deployee_index = args[int(args.index('-d')) + 1]
    wage_index = args[int(args.index('-o')) + 1]
    config_info(social_index,deployee_index,wage_index)
#    config_info.calc_course(wage,JSL,JSH,social_tax)
#except:
#    print("请输入正确的参数:")
#    print("python3 calculator.py [option] [parameter]" )
#    print("option:")
#    print("-c 指定社保比例配置文件名及目录")
#    print("-d 指定员工工资数据文件")
#    print("-o 指定计算后数据的输出目录及文件名")
#    print("例子:")
#    print("python3 calculator.py -c ./test.cfg -d ./user.csv -o /tmp/gongzi.csv")
#    sys.exit(-1)

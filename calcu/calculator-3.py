#!/usr/bin/env python3
import sys
import json

# read config info
point = int(3500)

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
        global wage_files
        # 将社保配置文件读取并存储到dict中
        wage_files = wage_file
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
    # 工资计算过程
class calc_course(object):
    def __init__(self,deployee,JSL,JSH,social_tax):
    # 社保应缴纳金额
        for key,value in deployee.items():
            if value <= JSL:
                socail_sum = format (JSL * social_tax,'.2f')
                self.calc_salary(key,social_sum)
            elif value > JSL and value <= JSH:
                social_sum = format(value * social_tax,'.2f')
                self.calc_salary(key,social_sum)
            elif value >JSH:
                social_sum = format(JSH * social_tax,'.2f')
                self.calc_salary(key,social_sum)
            line = str(str(key)+','+format(value,'.2f')+','+str(social_sum)+','+format(tax,'.2f')+','+format(salary,'.2f'))
            #print(line)
            with open(wage_files,'a+') as file:
                file.write(line + "\r\n")
                #salary_data = [str(key)+','+format(value,'.2f')+','+str(social_sum)+','+format(tax,'.2f')+','+format(salary,'.2f')]
                
            print(str(key)+','+format(value,'.2f')+','+str(social_sum)+','+format(tax,'.2f')+','+format(salary,'.2f'))
    def calc_salary(self,key,social_sum):
        # 个税金额
           global tax
           global salary
           tax_rate = float(deployee[key]) - float(social_sum) - float(point)
           if tax_rate < 0:
               tax = float(0)
               salary = int(deployee[key]) - tax - float(social_sum)
           elif tax_rate <= 1500:
               tax = float(format(float(tax_rate * 0.03 - 0)))
               salary = int(deployee[key]) - tax - float(social_sum)
           elif tax_rate > 1500 and tax_rate <= 4500:
               tax = float(format(float(tax_rate * 0.10 - 105)))
               salary = int(deployee[key]) - tax - float(social_sum)
           elif tax_rate > 4500 and tax_rate <= 9000:
               tax = float(format(float(tax_rate * 0.20 - 555)))
               salary = int(deployee[key]) - tax - float(social_sum)
           elif tax_rate > 9000 and tax_rate <= 35000:
               tax = float(format(float(tax_rate * 0.25 - 1005)))
               salary = int(deployee[key]) - tax - float(social_sum)
           elif tax_rate > 35000 and tax_rate <= 55000:
               tax = float(format(float(tax_rate * 0.30 - 2755)))
               salary = int(deployee[key]) - tax - float(social_sum)
           elif tax_rate > 55000 and tax_rate <= 80000:
               tax = float(format(float(tax_rate * 0.35 - 5505)))
               salary = int(deployee[key]) - tax - float(social_sum)
           elif tax_rate > 80000:
               tax = float(format(float(tax_rate * 0.45 - 13505)))
               salary = int(deployee[key]) - tax - float(social_sum)
            

    
if __name__ == '__main__':
    args = sys.argv[1:]
#try:
    social_index = args[int(args.index('-c')) + 1]
    deployee_index = args[int(args.index('-d')) + 1]
    wage_index = args[int(args.index('-o')) + 1]
    config_info(social_index,deployee_index,wage_index)
    calc_course(deployee,JSL,JSH,social_tax)
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

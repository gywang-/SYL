#!/usr/bin/env python3
# 2018-03-17
# coding=utf-8

import sys
insurance = float(0.165)
point = int(3500)

    # 税后计算公式
def furmula(wage,rapid,tax_rate):
    # insurance:保险税率
    # point 征收点
    # wage 税前工资
    # rapid 速算扣除数
    # tax_rate 税率
    try:
        ins_amount = wage * insurance
        payable = wage - ins_amount - point 
        tax = payable * tax_rate - rapid
        salary = format((wage - ins_amount - tax),".2f")
        return salary
    except:
        print("Paramenter Error")


# 多员工工资计算

def calc(Id,wage):
    salary = wage - point 
    wage_dict = {}
    if salary <= 0:
        wage_amount = furmula(wage,0,0)
    elif salary <= 1500:
        wage_amount = furmula(wage,0,0.03)
    elif salary <= 4500 and salary > 1500:
        wage_amount = furmula(wage,105,0.1)
    elif salary <= 9000 and salary > 4500:
        wage_amount = furmula(wage,555,0.2)
    elif salary <= 35000 and salary > 9000:
        wage_amount = furmula(wage,1005,0.25)
    elif salary <= 55000 and salary > 35000:
        wage_amount = furmula(wage,2555,0.3)
    elif salary <= 80000 and salary > 55000:
        wage_amount = furmula(wage,5505,0.35)
    elif salary > 80000:
        wage_amount = furmula(wage,13505,0.45)
    print(Id,end='')
    print(':',end='')
    print(wage_amount)

# 用户传参
for arg in sys.argv[1:]:
    deployee_list = arg.split(':')
    calc(int(deployee_list[0]),int(deployee_list[1]))


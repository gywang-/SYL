#!/usr/bin/env python3
# 2018-03-15
#

import sys
# 起征点
proint = int(3500)
# 异常处理
try:
    str = sys.argv[1]
except:
    print(ValueError)

salary = int(str) - proint
if salary <= 0:
    print(format(0,".2f"))
elif salary <= 1500 and salary > 0: 
    tax = format((salary * 0.03 - 0) ,".2f")
    print(tax)
elif salary > 1500 and salary <= 4500: 
    tax = format((salary * 0.1 - 105),".2f")
    print(tax)
elif salary > 4500 and salary <= 9000: 
    tax = format((salary * 0.2 - 555),".2f")
    print(tax)
elif salary > 9000 and salary <= 35000: 
    tax = format((salary * 0.25 - 1005),".2f")
    print(tax)
elif salary > 35000 and salary <= 55000: 
    tax = format((salary * 0.30 - 2755),".2f")
    print(tax)
elif salary > 55000 and salary <= 80000: 
    tax = format((salary * 0.35 - 5505),".2f")
    print(tax)
elif salary > 80000:
    tax = format((salary * 0.45 - 13505),".2f")
    print(tax)

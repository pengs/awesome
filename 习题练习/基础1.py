#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
编写程序，完成以下要求：
	提示用户进行输入数据
	获取用户的数据数据（需要获取2个）
	1、对获取的两个数字进行求和运行，并输出相应的结果
	2、对获取的两个数字进行减法运行，并输出相应的结果
'''
def add(num1,num2):
		return num1 + num2

def minus(num1,num2):
		return num1 - num2
	
input_data = input('''请输入数据:
1 是+
2 是-
输入你的选择（1/2):
''')
if input_data not in '12':
	print("输入的求数据的公式不正确")
else:
	num1 = int(input("请输入第一个数字:"))	
	num2 = int(input("请输入第二个数字:"))
	if input_data =='1':
		print("你选择两数相加，结果为:{}".format(num1 + num2))
	elif input_data =='2':
		print("你选择两数相减,结果为:{}".format(num1-num2))
	
	

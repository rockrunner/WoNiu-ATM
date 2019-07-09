#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from ATM包 import loading,register
#登录界面

class Atm:
    def __init__(self):
        self.enter()

    def enter(self):
        print('='*5+" 欢迎使用蜗牛ATM无限制存取款系统 "+'='*5)
        print('='*3+" 请输入你的选项 1:登录 2:注册 3:退出 "+'='*3)
        print('='*38)
        a = int(input())
        if a == 1:#登录
            loading.load().check1()
        elif a == 2:#注册
            register.reg().add()
            self.enter()
        elif a == 3:#退出
            print("提示：你已退出系统")
            exit()
        else:
            print("请输入相对应选项的数字！")
            self.enter()


#ATM操作系统
count=0
while 1:
    try:
        Atm()
        break
    except Exception:
        count += 1
        if count==3:
            print("恶意操作系统，错误次数已达上限，退出系统！")
            break
        print("系统重新开始，请做出相应对象的选择！")




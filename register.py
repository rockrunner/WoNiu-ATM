#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import re
from ATM包 import db_con
import time

#注册界面
class reg:
    def __init__(self):
        self.time0 = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())
    def add(self):
        print('='*5+"欢迎来到注册界面"+'='*5)
        print('=' * 5 + "请注册你的用户名"+'=' * 5)
        #用户名注册确认

        while True:
            username=input()
            pattern1 = re.compile("^[a-zA-Z0-9]{1,20}$")
            if (pattern1.search(username)):


                r = db_con.Db().select("select * from ATM where uname='%s'" % username)

                if len(r)==0:
                    break
                else:
                    print("用户名已存在，请重新注册")
            else:
                print("用户名只允许用数字与字母组合1-20位注册，请重新注册")
        print('=' * 5 + "请填写你的密码"+'=' * 5)

        #密码注册确认
        while True:
            userpasswd1 = input()
            pattern2= re.compile("^[a-zA-Z0-9]{1,20}$")
            if (pattern2.search(userpasswd1)):
                break
            else:
                print("密码只允许用数字与字母1-20位组合注册")
        #密码再次确认
        while True:
            print('=' * 5 + "请再次输入确认你的密码" + '=' * 5)
            userpasswd2 = input()
            if userpasswd2==userpasswd1:
                break
        #手机号码注册
        print('=' * 5 + "请填写你的手机号码" + '=' * 5)
        while True:
            userphone=input()
            pattern3= re.compile("^1[3-9][0-9]{9}$")
            if (pattern3.search(userphone)):
                print("恭喜你注册成功！请谨记你的账号和密码！")
                with open(r'F:\test\ATM包\atm注册信息.txt', mode='a+')as f:
                    f.write("用户%s在%s注册成功\n" % (username, self.time0,))
                break
            else:
                print("手机号码必须是11位数字且第一位为1，第二位为3-9")

        db_con.Db().add_db(username, userpasswd2, userphone)


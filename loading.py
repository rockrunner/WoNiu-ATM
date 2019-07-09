#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from ATM包 import db_con,control
import time
class load:
    def __init__(self):
        self.time0 = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())
    def check1(self):#开始检查用户名
        count1=0
        flag = True
        while True:
            print("请输入你的用户名：")

            name1 = input()

            r = db_con.Db().select("select * from ATM where uname='%s'" % name1)

            if len(r)==1:#开始检查密码
                count2 = 0
                while True:
                    print("请输入你的密码：")
                    passwd = input()

                    s = db_con.Db().select("select * from ATM where uname='%s'" %name1)

                    if s[0][1] == passwd:
                        print("登录成功!")
                        with open(r'F:\test\ATM包\atm登录信息.txt', mode='a+')as f:
                            f.write("用户%s在%s登录成功\n" % (name1, self.time0,))
                        flag=False
                        control.control().control1(name1)



                    else:
                        print("你输入的密码错误，请重新输入正确的密码")
                        count2 += 1
                        if count2 > 2:
                            print("你输入用户名错误次数已达到三次,退出系统")
                            flag=False
                            break
            else:
                print("你输入的用户名不存在，请重新输入正确的用户名")
                count1+=1
                if count1>2:
                    print("你输入用户名错误次数已达到三次，退出系统")
                    flag=False
            if flag==False:
                exit()




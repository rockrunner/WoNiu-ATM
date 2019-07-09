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

class control:
    def __init__(self):
        self.time0 = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())
    def t_account(self,str1):#转账的代码
        print('*' * 10 + "转账界面" + '*' * 10)
        flag2 = False
        while True:
            print("请输入你转账对象的用户名")
            str2 = input()
            r = db_con.Db().select("select * from ATM where uname='%s'" % str2)

            if len(r) == 0:
                print("你输入的用户名不存在，请重新输入")
            else:
                print("用户名存在，用户名验证成功")
                while True:
                    print("请输入你想转账的金额")
                    num = input()
                    pattern = re.compile("^[0-9]{1,9}$")
                    if (pattern.search(num) != None):
                        num = float(num)
                        info3 = db_con.Db().select("select * from ATM where uname='%s'" % str1)
                        if num > info3[0][3]:
                            print("你输入的转账金额已超过你当前账户余额，请输入正确的金额")
                        else:
                            db_con.Db().account(str2, str1, num)
                            info3 = db_con.Db().select("select * from ATM where uname='%s'" % str1)
                            print("向%s转账%f元成功，你当前的账户余额为：%f" % (str2, num, info3[0][3]))
                            with open(r'F:\test\ATM包\atm操作信息.txt', mode='a+')as f:
                                f.write("用户%s在%s向用户%s转了%f元，当前%s的账户余额（%f元）\n" % (str1,self.time0,str2, num, str1,info3[0][3]))
                            flag2 = True
                            break
                    else:
                        print("请重新输入正确格式的金额：数字，可以包含2位小数")
            if flag2 == True:
                break

        self.control1(str1)
    def d_account(self,str1):#取款的代码
        print('*' * 10 + "取款界面" + '*' * 10)
        while True:
            print("请输入你想取款的金额")
            num1 = input()
            pattern = re.compile("^[0-9]{1,9}$")
            if (pattern.search(num1) != None):
                num1 = float(num1)
                info2 = db_con.Db().select("select * from ATM where uname='%s'" % str1)
                if num1 > info2[0][3]:
                    print("你输入的取款金额已超过你当前账户余额，请输入正确的金额")
                else:
                    db_con.Db().draw_money(str1, num1)
                    info2 = db_con.Db().select("select * from ATM where uname='%s'" % str1)
                    print("取款成功，你当前的账户余额为：'%f'元" % info2[0][3])
                    with open(r'F:\test\ATM包\atm操作信息.txt', mode='a+')as f:
                        f.write("用户%s在%s取走了%f元，当前他的账户余额（%f元）\n" % (str1, self.time0, num1, info2[0][3]))
                    break
            else:
                print("请重新输入正确格式的金额：数字，可以包含2位小数")
        self.control1(str1)
    def a_account(self,str1):#存款的代码
        print('*' * 10 + "存款界面" + '*' * 10)
        while True:
            print("请输入你想存款的金额")
            num2 = input()
            pattern = re.compile("^[0-9]{1,9}$")
            if (pattern.search(num2) != None):
                num2 = float(num2)
                db_con.Db().add_money(str1, num2)
                info3 = db_con.Db().select("select * from ATM where uname='%s'" % str1)
                print("存款成功，你当前的账户余额为：%f元" % info3[0][3])
                with open(r'F:\test\ATM包\atm操作信息.txt', mode='a+')as f:
                    f.write("用户%s在%s存入了%f元，当前他的账户余额（%f元）\n" % (str1, self.time0,num2,info3[0][3]))
                break
            else:
                print("提示：请重新输入正确格式的金额；为数字，可以包含2位小数")
        self.control1(str1)

    def control1(self,str1):#操作界面

        print('=' * 10 + "请输入你的选项" + '=' * 10)
        print('=' * 2 + " 1：查询余额 2：转账 3：取款 4：存款 5: 返回主菜单 6：退出 " + '=' * 2)
        print('=' * 50)
        b = input()
        if b == '1':#查询余额
            print('*' * 10 + "查询界面" + '*' * 10)
            info = db_con.Db().select("select * from ATM where uname='%s'" %str1)
            print("你正在查询的账户余额为：%f元" % info[0][3])
            with open(r'F:\test\ATM包\atm操作信息.txt',mode='a+')as f:
                f.write("用户%s在%s查询了他的账户余额（%f元）\n"%(str1,self.time0,info[0][3]))
            self.control1(str1)
        elif b=='2':#转账
            self.t_account(str1)
        elif b=='3':#取款
            self.d_account(str1)
        elif b=='4':#存款
            self.a_account(str1)
        elif b=='5':#返回主菜单
            from ATM包 import atm
            atm.Atm().enter()
        elif b=='6':
            exit()
        else:
            print('请重新进行选择')
            self.control1(str1)





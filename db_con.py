#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import pymysql
#创建表
# cur.execute("drop table if exists ATM")
# sql = """create table ATM(
#   uname varchar(20) primary key,
#   upasswd int,
#   phone int
#   )"""
# cur.execute(sql)
#查询用户名
class Db:
    def __init__(self):
        pass
    def select(self,sql):
        db=pymysql.connect('localhost','root','123456','mysqlpy')
        cur=db.cursor()
        cur.execute(sql)
        datas=cur.fetchall()
        db.close()
        return datas
    #提取当前用户的信息
    def select_one(self,sql):
        db=pymysql.connect('localhost','root','123456','mysqlpy')
        cur=db.cursor()
        cur.execute(self,sql)
        datas=cur.fetchone()
        db.close()
        return datas
    #注册，增加用户
    def add_db(self,username, userpasswd, phone):
        db = pymysql.connect('localhost', 'root', '123456', 'mysqlpy')
        cur = db.cursor()
        sql = ("insert into ATM (uname,upasswd,phone,r_money) values ('%s','%s','%s','%f')" % (
        username, userpasswd, phone, 5000))
        cur.execute(sql)
        db.commit()
        db.close()

    #取款
    def draw_money(self,name,cost):
        db = pymysql.connect('localhost', 'root', '123456', 'mysqlpy')
        cur = db.cursor()
        sql_up = "update ATM set r_money=r_money-'%f' where uname='%s'" %(cost,name)
        cur.execute(sql_up)
        db.commit()
        db.close()
    #转账
    def account(self,name1,name2,cost1):
        db = pymysql.connect('localhost', 'root', '123456', 'mysqlpy')
        cur = db.cursor()
        sql_up = "update ATM set r_money=r_money+'%f' where uname='%s'"%(cost1,name1)
        sql_down="update ATM set r_money=r_money-'%f' where uname='%s'"%(cost1,name2)
        cur.execute(sql_up)
        cur.execute(sql_down)
        db.commit()
        db.close()
    #存款
    def add_money(self,name,cost):
        db = pymysql.connect('localhost', 'root', '123456', 'mysqlpy')
        cur = db.cursor()
        sql_up = "update ATM set r_money=r_money+'%f' where uname='%s'" % (cost, name)
        cur.execute(sql_up)
        db.commit()
        db.close()

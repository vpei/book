#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
#pip3 install mysql-connector
import mysql.connector
from cls import LocalFile

host = os.environ.get('host')
if(host == None):
    host = '192.168.8.5'
port = os.environ.get('port')
if(port == None):
    port = 3306
user = os.environ.get('user')
if(user == None):
    user = 'vpei'
passwd = os.environ.get('passwd')
if(passwd == None):
    passwd = 'password'
database = os.environ.get('database')
if(database == None):
    database = 'newbook'

class MySQL():
    def get_db():
        try:
            # 接收参数：user, password, host, port=3306, unix_socket and database
            mydb = mysql.connector.connect(host=host, port=port, user=user, passwd=passwd, database=database)
            # print(mydb)
            return mydb
        except Exception as ex:
            print('MySQL-Line-40-Exception:\n' + str(ex))
            LocalFile.write_LogFile('MySQL-29-Exception:\n' + str(ex)
                + '\r\nhost:' + host + 'port:' + port + 'user:' + user + 'passwd:' + passwd + 'database:' + database)
            return ''

    def get_table_one(sql):
        data = ''
        try:
            # 打开数据库连接 返回一个MySQLConnection Object
            db = MySQL.get_db()
            # 使用cursor()方法获取操作游标 
            cursor = db.cursor()
            # 使用execute方法执行SQL语句
            cursor.execute(sql)
            # 使用 fetchone() 方法获取多条数据 fetchall() 方法获取多条数据
            data = cursor.fetchone()
            #print "Database version : %s " % data
            # 关闭数据库连接
            db.close()
            if(data == None):
                data = ''
        except Exception as ex:
            print('MySQL-49-Exception:\n' + str(ex))
        return data

    def get_table(sql):
        data = ''
        try:
            db = MySQL.get_db()
            cursor = db.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            db.close()
            if(data == None):
                data = ''
        except Exception as ex:
            print('MySQL-63-Exception:\n' + str(ex))
        return data

    def get_cont(sql):
        data = ''
        try:
            db = MySQL.get_db()
            cursor = db.cursor()
            cursor.execute(sql)
            data = cursor.fetchone()
            db.close()
            if(data == None):
                data = ''
        except Exception as ex:
            print('MySQL-77-Exception:\n' + str(ex))
        return data

    def mysql_execute(sql):
        data = ''
        try:
            mysql = MySQL.get_db()
            cursor = mysql.cursor()
            try:
                # 执行SQL语句
                cursor.execute(sql)
                # 提交到数据库执行
                mysql.commit()
                data = '1'
            except Exception as e:
                print(e)
                # 发生错误时回滚
                mysql.rollback()
                data = '0'
            mysql.close()
        except Exception as ex:
            print('MySQL-77-Exception:\n' + str(ex))
            data = '0'
        return data

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import re
# import sys
# sys.path.append('..')
from cls import LocalFile, MySQL
# from cls import LocalFile
# from cls.MySQL import MySQL

class Books():
    def get_book_info(id):
        jsontext = {'books':[]}     # 默认返回空字典数据格式
        # response_header = "HTTP/1.1 404 Not Found\r\nServer: PWS1.0"
        # response_body = 'Sorry, File Not Found'
        response_header = 'HTTP/1.1 200 OK\r\nServer: PWS1.0'
        response_body = 'index'
        try:
            LocalFile.write_LogFile('ID:' + id)
            zid = 0
            md5 = ''
            md5_reported = ''
            title = ''
            author = ''
            publisher = ''
            description = ''
            extension = ''
            language = ''
            year = ''
            cid = ''
            data = ''
            # 通过MD5查询记录
            if(len(id) == 32 and id.isalnum() == True):
                data = MySQL.get_table_one('select zlibrary_id, extension, md5, md5_reported, title, author, publisher, language, year, description from books where md5 = \'' + id + '\' or md5_reported = \'' + id + '\'')
            elif(id.isdigit() == True):
                if(int(id) > 22433982):
                    data = MySQL.get_table_one('select zlibrary_id from isbn where isbn = \'' + id + '\'')
                    if(data != ''):
                        id = str(data[0])
                zid = id
                data = MySQL.get_table_one('select zlibrary_id, extension, md5, md5_reported, title, author, publisher, language, year, description from books where zlibrary_id = ' + id)
            else:
                id = 0
                data = MySQL.get_table_one('select zlibrary_id, extension, md5, md5_reported, title, author, publisher, language, year, description from books where title like \'%' + id + '%\' limit 30')
                # 查询图书
            if(data != ''):
                zid = data[0]
                extension = data[1]
                md5 = data[2]
                if(md5 == None):
                    md5 = ''
                md5_reported = data[3]
                title = data[4]
                author = data[5]
                publisher = data[6]
                language = data[7]
                year = data[8]
                description = data[9]
                description = re.sub('<[^<]+?>', '', description).replace('\n', '').strip()
                if(cid == ''):
                    data = MySQL.get_cont('select cid from zlib12 where id = ' + str(zid))
                    if(data != ''):
                        cid = data[0]
                    if(cid == ''):
                        data = MySQL.get_cont('select cid from libgen where md5 = \'' + md5 + '\' or md5 = \'' + md5_reported + '\'')
                        if(data != ''):
                            cid = data[0]
                        if(cid == ''):
                            data = MySQL.get_cont('select cid from zlib122 where id = \'' + md5 + '\' or md5 = \'' + md5_reported + '\'')
                            if(data != ''):
                                cid = data[0]
                # for j in data:
                #     print(j[0]) # 处理多条记录
            response_data = ''
            response_header = ''
            response_body = ''
            nodeurl = ''
            if(len(cid) >= 46):
                # 临时测试数据
                jsontext['books'].append({'zid': str(zid), 'md5': md5, 'title': title, 'author': author, 'language': language, 'year': year, 'publisher': publisher, 'description': description, 'extension': extension, 'cid': cid})
                LocalFile.write_LogFile('\n' + str(jsontext))
                response_header = 'HTTP/1.1 200 OK\r\nServer: PWS1.0'    # 响应头
                # response_body = nodeurl                                # 响应体
                response_body = json.dumps(jsontext, indent=2, ensure_ascii=False)
            # response_header = 'HTTP/1.1 301 Moved Permanently\r\nServer: PWS1.0\r\nLocation: ' + nodeurl
            # #response_header = "HTTP/1.1 302 Moved Temporarily\r\nServer: PWS1.0"
            # response_body = ''
        except Exception as ex:
            ex = 'Main-Line-110-Exception:\n' + str(ex)
            print(ex)
            LocalFile.write_LogFile(ex)
        response_data = (response_header + '\r\n\r\n' + response_body).encode('utf-8')   # 将数据组装成HTTP响应报文数据发送给浏览器
        return response_data
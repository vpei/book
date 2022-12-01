#!/usr/bin/env python3

import os
import sys
from cls import LocalFile
from cls import StrText

# 获取传递的参数
try:
    #0表示文件名，1后面都是参数 0.py, 1, 2, 3
    menu = sys.argv[1:][0]
    if(len(sys.argv[1:]) > 1):
        cid = sys.argv[1:][1]
except:
    menu = 'all'
print('menu: ' + menu)

menu = 'all'

if(menu == 'libgen'):
    alltxt = ''
    path = "./html/libgen" #文件夹目录
    files= os.listdir(path) #得到文件夹下的所有文件名称
    i = 0
    for file in files: #遍历文件夹
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            i += 1
            print('正在处理文件-' + str(i))
            txt = LocalFile.read_LocalFile(path + '/' + file)
            ii = 0
            if(txt.find('</html>') == -1):
                LocalFile.write_LogFile('Main-Line-30-Exception:' + str(ex) + '\nj:' + j)
            for j in txt.split('\n'):
                try:
                    ii += 1
                    if(j.find('?filename=') > -1):
                        #j = StrText.get_str_btw(j, 'href="', '"', 0).replace('?filename=', ' ') + '\r\n'
                        alltxt += StrText.get_str_btw(j, '/ipfs/', '"', 0).replace('?filename=', ' ') + '\n'
                except Exception as ex:
                    LocalFile.write_LogFile('Main-Line-40-Exception:' + str(ex) + '\nj:' + j)
            fileint = int(file.split('.')[0])
            if(i % 300 == 0):
                filename = 'libgen-' + str(i/300) + '.txt'
                LocalFile.write_LocalFile(path.replace('html', 'cid') + '/' + filename, alltxt.strip('\n'))
                alltxt = ''
    filename = 'libgen-11.txt'
    LocalFile.write_LocalFile(path.replace('html', 'cid') + '/' + filename, alltxt.strip('\n'))
    alltxt = ''

if(menu == 'one'):
    path = './html/zlib2' #文件夹目录
    files= os.listdir(path) #得到文件夹下的所有文件名称
    i = 0
    for file in files: #遍历文件夹
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            i += 1
            print('正在处理文件-' + str(i))
            txt = LocalFile.read_LocalFile(path + '/' + file)
            if(txt.find('</html>') == -1):
                LocalFile.write_LogFile('Main-Line-30-Exception:' + str(ex) + '\nj:' + j)
            ii = 0
            alltxt = ''
            for j in txt.split('\n'):
                try:
                    ii += 1
                    if(j.find('?filename=') > -1):
                        #j = StrText.get_str_btw(j, 'href="', '"', 0).replace('?filename=', ' ') + '\r\n'
                        alltxt += StrText.get_str_btw(j, '/ipfs/', '"', 0).replace('?filename=', ' ') + '\n'
                except Exception as ex:
                    LocalFile.write_LogFile('Main-Line-149-Exception:' + str(ex) + '\nj:' + j)
            LocalFile.write_LocalFile(path.replace('html', 'cid') + '/' + file, alltxt.strip('\n'))
            alltxt = ''
            
if(menu == 'all'):
    path = './cid/libgen' #文件夹目录
    files= os.listdir(path) #得到文件夹下的所有文件名称
    i = 0
    alltxt = ''
    for file in files: #遍历文件夹
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            i += 1
            print('正在处理文件-' + str(i))
            txt = LocalFile.read_LocalFile(path + '/' + file)
            alltxt += txt + '\n'
    LocalFile.write_LocalFile(path + '-all-ipfs-cid-1123.txt', alltxt.strip('\n'))
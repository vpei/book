#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import base64
import requests
class Ipfs():

    # 从字符中取两不同字符串中间的字符，print(sub_link)，参数：文本，第一字符串，第二字符串，是否保留字符串
    def get_str_btw(s, f, b, y):
        par = s.partition(f)
        if(y == 0):
            return (par[2].partition(b))[0][:]
        else:
            return f + '' + (par[2].partition(b))[0][:] + '' + b

    # 读取本地节点文件
    def read_txt(file_path):
        file = open(file_path, 'rb')
        file_data = file.read()
        file.close()
        return file_data

    # 从网络文件是否存在
    def url_stat(r_url, linktime, readtime):
        retxt = 0
        try:
            requests.adapters.DEFAULT_RETRIES = 3 # 增加重连次数
            s = requests.session()
            s.keep_alive = False # 关闭多余连接
            rq = s.get(r_url, timeout=(linktime, readtime))
            retxt = rq.status_code
            rq.close()
        except Exception as ex:
            print('\nNetFile-Line-34: down res file err: ' + str(ex) + '\n' +  r_url)
        return retxt

    # Base64加密文本转换为标准格式
    def get_str_base64(origStr):
        missing_padding = 4 - len(origStr) % 4 
        if missing_padding: 
            origStr += '=' * missing_padding
        return origStr

    def get_info(url):
        try:
            if(url.find('/ipfs/') > -1):
                url = '/ipfs/' + url.rsplit('/ipfs/', 1)[1]
            elif(url.find('/ipns/') > -1):
                url = '/ipns/' + url.rsplit('/ipns/', 1)[1]
            else:
                url = '/ipfs/' + url
            ipfs = Ipfs.read_txt('ipfs.txt')
            ipfs = Ipfs.get_str_base64(ipfs.decode('utf-8'))
            ipfs = base64.b64decode(ipfs.encode('utf-8')).decode('utf-8').replace('\r','')
            node = ipfs.split('\n')
            # 处理IPFS URL如果随机生成的文件不存在，则按节点顺序进行检查
            # nodeurl = node[(int(zid) % len(node))] + '/ipfs/' + cid
            # ustat = ipfs.url_stat(nodeurl, 5, 5)
            # if(ustat != 200):
            for nodeurl in node:
                nurl = nodeurl + '' + url
                ustat = Ipfs.url_stat(nurl, 3, 3)
                if(ustat == 200):
                    url = nurl
                    break
        except Exception as ex:
            print(f"Book-79-Exception:{ex}")
        if(url.find('http://') == -1 and url.find('https://') == -1):
            url = 'https://ipfs.io' + url
        response_header = 'HTTP/1.1 301 Moved Permanently\r\nServer: PWS1.0\r\nLocation: ' + url
        response_data = (response_header + '\r\n\r\n').encode('utf-8')   # 将数据组装成HTTP响应报文数据发送给浏览器
        return response_data
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests,threading,time,random

class Messy:
    def __init__(self):
        self.__messy = 0

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
            #print('\nNetFile-Line-34: down res file err: ' + str(ex) + '\n' +  r_url)
            retxt = ''
        return retxt

    def m(self, i):
		# 随机时间进行打印
        time.sleep(random.random() * 2)
        print(i)
        if i == 1:
            self.__messy = 1

    def main(self):
        Threads = []
        # 将会启动10个线程, 线程id为 1 时全部线程终止！
        for i in range(10):
            t = threading.Thread(target=self.m, args=(i,))
            t.daemon = 1
            Threads.append(t)
        # 启动所有线程
        for i in Threads:
            i.start()
        # 当标志位【 messy 】时所有多线程结束
        while 1:
            if self.__messy:
                break
        print('线程已退出!')

Messy().main()
# 继续执行后续程序
for i in range(5):
    print('yeah!')

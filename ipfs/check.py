#!/usr/bin/python3

import queue
import requests
import threading
import time

exitFlag = 0
url = ''
reurl = ''

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
        
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

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
    
def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            data = url_stat(data, 10, 10)
            queueLock.release()
            reurl = data
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []

def get_ipfs(url):
    if(url.find('/ipfs/') > -1):
        url = '/ipfs/' + url.rsplit('/ipfs/', 1)[1]
    elif(url.find('/ipns/') > -1):
        url = '/ipns/' + url.rsplit('/ipns/', 1)[1]
    else:
        url = '/ipfs/' + url

    threadID = 1
    threadList = ["Thread-1", "Thread-2", "Thread-3"]
    nameList = ["http://81.68.68.232:8080", "http://220.243.137.16:8080", "http://223.111.148.196:8080", "http://14.215.165.43:8080", "http://133.18.228.34:8080"]
    # 创建新线程
    #for tName in threadList:
    for tName in nameList:
        #thread = myThread(threadID, tName, workQueue)
        thread = myThread(threadID, 'T_' + str(threadID), workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1

    # 填充队列
    queueLock.acquire()
    for word in nameList:
        workQueue.put(word + '' + url)
    queueLock.release()

    # 等待队列清空
    while not workQueue.empty():
        pass

    while (reurl!=''):
        return reurl

    # 通知线程是时候退出
    exitFlag = 1

    # 等待所有线程完成
    for t in threads:
        t.join()
    print ("退出主线程")
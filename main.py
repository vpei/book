#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
from books import Books
from cls import LocalFile
from cls import StrText

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # 创建TCP服务端套接字
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)  # 设置端口号复用，程序退出端口立即释放
    server_socket.bind(('', 8282))  # 绑定端口
    server_socket.listen(128)       # 设置监听线程
    while True:                     # 循环接受客户端的连接请求
        try:
            print('\n\nService is running...')
            comm_socket, ip_port = server_socket.accept()       # 等待接受客户端的连接请求
            recv_data = comm_socket.recv(4096).decode('utf-8')  # 获取浏览器发送的http请求报文数据, 每次发送4096数据字节
            if(recv_data != ''):
                print('Decoding the received data:\n', recv_data.strip('\n'))
            # GET /3feaca47d82f5900c53ab0082c778957 HTTP/1.1
            id = StrText.get_str_btw(recv_data, 'GET ', ' ', 0).strip('/')
            response_data = Books.get_book_info(id)
            comm_socket.send(response_data) # 发送响应报文数据至浏览器
            comm_socket.close()             # 关闭服务于客户端的套接字
        except Exception as ex:
            print('\nMain-32-Exception:' + str(ex))
            LocalFile.write_LogFile('Main-Line-70-Exception:\n' + str(ex))# + '\r\nrecv_data:' + recv_data.decode('utf-8'))
    # 关闭监听套接字
    # server_socket.close()
    # print('The service has been stopped.')
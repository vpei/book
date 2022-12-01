#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
from ipfs import Ipfs

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # 创建TCP服务端套接字
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)  # 设置端口号复用，程序退出端口立即释放
    server_socket.bind(('', 8383))  # 绑定端口
    server_socket.listen(128)       # 设置监听线程
    while True:                     # 循环接受客户端的连接请求
        try:
            print('\n\nService is running...')
            comm_socket, ip_port = server_socket.accept()       # 等待接受客户端的连接请求
            recv_data = comm_socket.recv(4096).decode('utf-8')  # 获取浏览器发送的http请求报文数据, 每次发送4096数据字节
            if(recv_data != ''):
                print('Decoding the received data:\n', recv_data.strip('\n'))
                # GET /3feaca47d82f5900c53ab0082c778957 HTTP/1.1
                url = Ipfs.get_str_btw(recv_data, 'GET ', ' ', 0).strip('/')
                if(url == ''):
                    # 分割http响应头和响应body
                    response_data = ('HTTP/1.1 200 OK\r\nServer: PWS1.0\r\n\r\n' + read_html('./cha.html')).encode('utf-8')
                else:
                    response_data = Ipfs.get_info(url)
            comm_socket.send(response_data) # 发送响应报文数据至浏览器
            comm_socket.close()             # 关闭服务于客户端的套接字
        except Exception as ex:
            print('\nMain-25-Exception:' + str(ex))
    # 关闭监听套接字
    # server_socket.close()
    # print('The service has been stopped.')
    
def read_html(file_path):
    file = open(file_path, 'rb')
    file_data = file.read()
    file.close()
    return file_data.decode('utf-8')

if __name__ == '__main__':
    main()
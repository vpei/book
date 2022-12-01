# 编写自己的web服务器，发送html页面
# http是给予TCP实现的
import socket
import re


def service_client(new_socket):
    request = new_socket.recv(1024).decode("utf-8")
    print(request)

    request_line = request.splitlines()
    try:
        res = re.match(r"[^/]+(/[^ ]*)", request_line[0])
        file_name = res.group(1)

        if file_name == '/':
            file_name = '/index.html'
        response_head = "HTTP/1.1 200 OK\r\n"
        # 分割http响应头和响应body
        response_head += '\r\n'
        response_body = read_html("html"+file_name)

        new_socket.send(response_head.encode('utf-8'))
        new_socket.send(response_body)
        new_socket.close()
    except IndexError:
        pass

def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时可以立即绑定9090端口
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    # 2. 绑定
    tcp_server_socket.bind(("", 9090))
    # 3. 监听套接字
    tcp_server_socket.listen(128)
    while True:
        # 4. 等待连接
        new_socket, client_addr = tcp_server_socket.accept()
        # 5. 发送数据
        service_client(new_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


def read_html(file_path):
    file = open(file_path, 'rb')
    file_data = file.read()
    file.close()
    return file_data


if __name__ == '__main__':
    main()
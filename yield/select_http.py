# epoll select

# 在高并发的情况下，连接活跃度不是很高，epoll 比select 好
# 并发性不高，同时连接很活跃 select比 epool好

# 非阻塞io带来的好处
# 非阻塞io实现http
import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()

flag = False


class Fetcher:
    def __init__(self):
        self.client = None
        self.data = b""

    def connected(self, key):
        print(key)
        selector.unregister(key.fd)
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            pass
            self.client.close()
            global flag
            flag = True

    def get_url(self, url):
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        if self.path == "":
            self.path = "/"

        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))  # 阻塞不会消耗cpu
        except BlockingIOError as e:
            pass
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    # select 本身不支持register
    # socket状态变化以后的回掉是有程序完成的
    while flag:
        ready = selector.select()
        for k, v in ready:
            callback = k.data
            callback(k)


if __name__ == "__main__":
    # epool linux
    fet = Fetcher()
    fet.get_url("http:/www.baidu.com")
    loop()

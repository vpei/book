#!/bin/bash

# cd / && rm -rf /bookbot && git clone https://gitclone.com/github.com/vpei/book.git bookbot && rm -rf /bookbot/.git
# mkdir /root/book/ && mv /book/* /root/book/ && rm -rf /book

cd / && rm -rf /bookbot && wget https://raw.githubusercontent.com/vpei/book/main/book.zip -O bookbot.zip && unzip -d /bookbot/ bookbot.zip && rm -rf /bookbot.zip

# nohup aria2c --conf-path=/root/.aria2/aria2.conf --rpc-listen-port=8080 --rpc-secret=$Aria2_secret &

# nohup python3 /book/main.py &
cd /bookbot/ && python3 main.py

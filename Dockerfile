# 设置继承的镜 alpine # 180M < debian # 688M < ubuntu # 1.1G
FROM alpine:latest
# FROM debian:unstable-slim
# FROM ubuntu:latest
# 下面是一些创建者的基本信息

MAINTAINER debian + python3 + booksearch (vpei@live.com)

# 在终端需要执行的命令
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
# RUN sed -ri -e 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources
# RUN sed -ri -e 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
# 添加镜像
# RUN sed '$a deb http://archive.ubuntu.com/ubuntu/ trusty main universe restricted multiverse' /etc/apt/sources.list
# # 仅限linux使用
# RUN apt update
# 仅限alpine使用
RUN apk update
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
RUN apk add --update tzdata
RUN apk add --update bash
RUN apk add --update wget
RUN apk add --update git
RUN apk add --update python3-dev
# # 仅限linux使用
# RUN apk add --update python3-pip
# 仅限alpine使用
RUN apk add --update py3-pip
# RUN apk add --update curl
# RUN apk add --update vim
RUN apk add --update unzip
# RUN apk add --update python3-pillow
# RUN apk add --update gcc libffi-dev libssl-dev 
# RUN apk add --update libxml2-dev libxslt-dev
# RUN apk add --update gconf-service libasound2 libatk1.0-0 libatk-bridge2.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

# pip3安装Python3的项目依赖库
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple mysql-connector
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple re
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pillow
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple mutagen
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -U yt-dlp
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple apschedule
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pyromod
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple psutil
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple nest_asyncio
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pyppetee

# 解析网页内容
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple beautifulsoup4 #li格式
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple lxml --upgrade
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple bs4            # 默认lxml，修改bs4超链接
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple html5lib       # 默认lxml，修改bs4超链接 
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas         #table格式 
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple meilisearch         #meilisearch 

# 解决alpine bash: not found 错误
# RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

# COPY . /book
# RUN cd / && chmod 7777 -R /book && mv ./book/start.sh / && sed -i 's/\r//' start.sh
# CMD chmod 7777 start.sh && bash start.sh
CMD wget https://ghproxy.com/https://raw.githubusercontent.com/vpei/book/main/start.sh -O start.sh && chmod 0777 start.sh && sed -i 's/\r//' start.sh && bash start.sh

# 打包命令
# docker login && docker buildx build -t vpei/book:latest --platform linux/amd64 --push .

# 批量打包命令
# docker buildx install
# docker buildx create --use --name build --node build --driver-opt network=host
# docker login && docker buildx build -t vpei/book:latest --platform linux/arm/v7,linux/arm64/v8,linux/386,linux/amd64 --push .

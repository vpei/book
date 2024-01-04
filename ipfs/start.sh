#!/bin/bash

cd / && rm -rf /ipfs && wget https://raw.githubusercontent.com/vpei/book/main/ipfs/ipfs.zip -O ipfs.zip && unzip -d /ipfs/ ipfs.zip && rm -rf /ipfs.zip

# cd /ipfs/ && python3 sleep.py
cd /ipfs/ && python3 main.py

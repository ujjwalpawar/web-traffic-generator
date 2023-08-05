#!/bin/bash

timeout 600 mpv https://www.dailymotion.com/video/x7eklbf --vo=null -v | tee install.log

sleep 30

timeout 600 wget -o- https://speed.hetzner.de/1GB.bin | tee install.log

sleep 30

timeout 600 python gen.py > logs_web | tee install.log

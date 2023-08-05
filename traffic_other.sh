#!/bin/bash

timeout 6 mpv https://www.dailymotion.com/video/x7eklbf --vo=null -v

sleep 3

timeout 6 wget -o- https://speed.hetzner.de/1GB.bin

sleep 3

timeout 6 python gen.py

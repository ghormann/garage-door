#!/bin/sh
cd /home/pi/src/opendoor
./door.py >> logs/log.txt 2>&1

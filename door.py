#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

PIN=7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.LOW)

def trigger():
   GPIO.output(PIN, GPIO.HIGH)
   time.sleep(0.2)
   GPIO.output(PIN, GPIO.LOW)

trigger()

GPIO.cleanup()

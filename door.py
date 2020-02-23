#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
from flask import Flask, request, redirect, send_from_directory

app = Flask(__name__, static_url_path='')
PIN=7

##############################################3

@app.route("/trigger", methods=['GET', 'POST'])
def trigger():
   GPIO.output(PIN, GPIO.HIGH)
   time.sleep(0.2)
   GPIO.output(PIN, GPIO.LOW)
   return redirect("/static/index.html")


@app.route("/", methods=['GET'])
def handle_main():
   return redirect("/static/index.html")


@app.route("/static/<path:path>", methods=['GET'])
def send_static(path):
   return send_from_directory('static', path)

if __name__ == "__main__":
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(PIN, GPIO.OUT)
   GPIO.output(PIN, GPIO.LOW)
   app.run(host='0.0.0.0', port=8080)

#GPIO.cleanup()

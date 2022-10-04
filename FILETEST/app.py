import os
from flask import Flask, send_from_directory
from multiprocessing import Process
import requests
import time
import os

def busytask():
  while True:
    time.sleep(20)
    requests.get("https://google.com")
    os.system("./busywork.sh")

p = Process(target=busytask)
p.daemon = True
p.start()

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
  return "Hello world!"

@app.route('/vod')
def vidios():
  return send_from_directory('/home/runner/Downloads/',os.listdir('/home/runner/Downloads/')[0])


app.run(host='0.0.0.0', port=8080)
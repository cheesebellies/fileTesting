import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
  return "Hello world!"

@app.route('/vod')
def vidios():
  return send_from_directory('/home/runner/Downloads/',os.listdir('/home/runner/Downloads/')[0])

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
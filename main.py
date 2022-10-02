import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time
import os
import ast
import flask
from flask import Flask, send_from_directory

l = ["seltest2","middleman","lastman"]
for i in l:
  requests.get(f"https://{i}.david0weir.repl.co/")

url = (requests.post("https://seltest2.david0weir.repl.co/search",{'tosearch':'moana'}).text)

# cookies = requests.get("https://lastman.david0weir.repl.co/cookies").text
# print(cookies)
# cookies = ast.literal_eval(cookies)
# print(cookies)

print(url)

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.google.com/")

# for i in cookies:
#   driver.add_cookie(i)


driver.get(url)

result = driver.find_element(By.TAG_NAME, "video").get_attribute("src")
print(result)

driver.get(result)
sa = 0
while True:
  sa+= 1
  time.sleep(300)
  driver.get("https://google.com")
  if sa == 7:
    break

input("wait for download")

driver.close()

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
  return "Hello world!"

@app.route('/vod')
def vidios(path):
  return send_from_directory('~/Downloads/',os.listdir('~/Downloads/')[0])

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
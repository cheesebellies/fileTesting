import requests
import selenium
from tqdm import tqdm
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time
import os
import ast
import subprocess
import flask
from loadingbar import Bar
from flask import Flask, send_from_directory
from replit import db

db["isdone"]=False
db["progress"] = 1
db["info"] = ''

class Downloader:

  def __init__(self):
    pass
    
  def initp(self):
    db["progress"] = 2
    l = ["seltest2","middleman","lastman"]
    for i in l:
      requests.get(f"https://{i}.david0weir.repl.co/")

  def geturl(self,info):
    db["progress"] = 3
    db["info"] = info
    url = (requests.post("https://seltest2.david0weir.repl.co/search",{'tosearch':info}).text)
    return url
  
  # cookies = requests.get("https://lastman.david0weir.repl.co/cookies").text
  # print(cookies)
  # cookies = ast.literal_eval(cookies)
  # print(cookies)
  def dlurl(self,url):
    print(url)
    db["progress"] = 4
    db["info"] = str(url)
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
    time.sleep(10)
    bar = Bar()
    p = Process(target=bar.Start)
    p.daemon = True
    p.start()
    while True:
      sa+= 1
      time.sleep(300)
      driver.get("https://google.com")
      if sa == 10:
        break
    
    while True:
      time.sleep(5)
      if db["isdone"] == True:
        print("GO TO https://FILETEST.david0weir.repl.co/vod to download video!!")
        break


class Start:

  def __init__(self,tosearch):
    self.dlr = Downloader()
    self.tosearch = tosearch
    

  def start(self):
    self.dlr.initp()
    url = self.dlr.geturl(self.tosearch)
    self.dlr.dlurl(url)
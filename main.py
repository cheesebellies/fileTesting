import requests
# import selenium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import json
import time

# chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_experimental_option("detach", True)
  
# driver = webdriver.Chrome(options=chrome_options)
l = ["seltest2","middleman","lastman"]
for i in l:
  requests.get(f"https://{i}.david0weir.repl.co/")

time.sleep(20)
url = (requests.post("https://seltest2.david0weir.repl.co/search",{'tosearch':'moana'}).text)

print(url)
# driver.get(url)
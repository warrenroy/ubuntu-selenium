import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = 'insert_url_here'

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--window-size=1920,1200')
DRIVER_PATH = '/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

try:
   file = open('list.txt')
   for line in file:
      line = line.strip()
      driver.get($URL+line)
      export = open(line+'.txt', 'x')
      export.write(driver.page_source)
      export.close()
finally:
   file.close()
driver.quit()

import os
import time
import requests

while True:
    time.sleep(5)
    files = os.listdir('/var/log')
    num_errors = len(files)
    if num_files >= 1:
        requests.post(WEBSERVER_URL + f"/critical", "Critical number of logs received")
  

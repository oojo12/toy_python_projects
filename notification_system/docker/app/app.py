import os
import random
import requests

WEBSEVER_URL = os.environ['WEBSERVER_URL']
LOG_TYPES = ['info', 'warning', 'error']

messages_sent = 0
while True:
    message = {
        'From': "a@example.com",
        "To": "b@example.com",
        "Subject": f"{LOG_TYPES[random.randint(len(LOG_TYPES)]}",
        "Message-ID": f"<ant> {LOG_TYPES[random.randint(len(LOG_TYPES)]}"
    }
    requests.post(WEBSERVER_URL, message)
    messages_sent += 1
    if messages_sent == 10:
        break

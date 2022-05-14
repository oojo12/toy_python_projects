import os
import random
import requests

WEBSEVER_URL = os.environ['WEBSERVER_URL']
LOG_TYPES = ['info', 'warning', 'error']

messages_sent = 0
while True:
    log_type = LOG_TYPES[random.randint(len(LOG_TYPES))
    message = {
        'From': "a@example.com",
        "To": "b@example.com",
        "Subject": f"{log_type}",
        "Message-ID": f"<ant> {log_type}"
    }
    requests.post(WEBSERVER_URL + f"/{log_type}", message)
    messages_sent += 1
    if messages_sent == 10:
        break

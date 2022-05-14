import os
from fastapi import FastAPI
from smtplib import SMTP as Client

HOSTNAME, PORT = os.environ['SMTP_HOSTNAME'], os.environ['SMTP_PORT']


app = FastAPI()

client = Client(HOSTNAME, PORT)

def _fornat_message(payload):
    message = {}
    for key in payload:
        message[key] = payload[key]
    return message
  
def _send_message(message):
    r = client.sendmail(payload['From'], payload['To'],
                        f"""
                        From: {payload['From']}
                        To: {payload['To']}
                        Subject: {payload['Subject']}
                        Message-ID: {payload['Message-ID']}
                        """
                       )
    
@app.get("/error")
async def error(payload):
    message = _format_message(payload)
    _send_message(message)

@app.get("/warning")
async def error(payload):
    message = _format_message(payload)
    _send_message(message)

@app.get("/info")
async def error(payload):
    message = _format_message(payload)
    _send_message(message)


@app.get("/critical")
async def error(payload):
    message = _format_message(payload)
    _send_message(message)

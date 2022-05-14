import asyncio
from smtplib import SMTP as Client
from aiosmtpd.controller import Controller

class ExampleHandler:
 async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
     if not address.endswith('@example.com'):
         return '550 not relaying to that domain'
     envelope.rcpt_tos.append(address)
     return '250 OK'

 async def handle_DATA(self, server, session, envelope):
     print('Message from %s' % envelope.mail_from)
     print('Message for %s' % envelope.rcpt_tos)
     print('Message data:\n')
     for ln in envelope.content.decode('utf8', errors='replace').splitlines():
         print(f' {ln}'.strip())
     print()
     print('End of message')
     return '250 Message accepted for delivery'


controller = Controller(ExampleHandler())
controller.start()


client = Client(controller.hostname, controller.port)
r = client.sendmail('a@example.com', ['b@example.com'], """\
 From: Anne Person <anne@example.com>
 To: Bart Person <bart@example.com>
 Subject: A test
 Message-ID: <ant>

 Hi Bart, this is Anne.
 """)


controller.stop()

# -*- coding: utf-8 -*-
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from initial import Email


class EmailSender(object):
    def __init__(self, text):
        self.ini = Email()
        self.msg = MIMEText(text, 'plain', 'utf-8')

    @staticmethod
    def _format(s):
        name, address = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), address))

    def _from(self):
        self.msg['From'] = self._format(self.ini.from_addr)

    def _to(self):
        self.msg['To'] = self._format(self.ini.to_addr)

    def _subject(self):
        self.msg['Subject'] = Header(self.ini.header, 'utf-8').encode()

    def send(self):
        server = SMTP(self.ini.server)
        self._from()
        self._to()
        self._subject()
        server.sendmail(self.ini.from_addr, eval(self.ini.to_addr),  self.msg.as_string())
        server.quit()

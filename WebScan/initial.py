# -*- coding: utf-8 -*-
import configparser
import ast
import sys
import os


class Default(object):
    def __init__(self):
        self._config = configparser.ConfigParser()
        self.local_path = sys.path[0]
        self._config.read(os.path.join(self.local_path, 'Profile.ini'))

    @property
    def default_vpn(self):
        return self._config.defaults().get('defaultvpn')

    @property
    def loading_timeout(self):
        return self._config.defaults().get('loading_timeout')


class Requests(Default):
    def __init__(self):
        Default.__init__(self)

    @property
    def proxies(self):
        proxies = self._config.get('requests', 'proxies')
        return None if proxies == '' else ast.literal_eval(proxies)

    @property
    def timeout(self):
        return self._config.getint('requests', 'timeout')

    @property
    def allow_redirects(self):
        return self._config['requests']['allow_redirects']


class Urllib(Default):
    def __init__(self):
        Default.__init__(self)

    @property
    def proxy_host(self):
        return self._config.get('urllib', 'proxy_host')

    @property
    def proxy_type(self):
        return self._config.get('urllib', 'proxy_type')

    @property
    def timeout(self):
        return self._config.getint('urllib', 'timeout')


class AstrillInitial(Default):
    def __init__(self):
        Default.__init__(self)
        self._astrill = self._config['ASTRILL']

    @property
    def cmd_line(self):
        return self._astrill['cmd_line']

    @property
    def path(self):
        return self._astrill['path']

    @property
    def timeout(self):
        return self._astrill['timeout']

    @property
    def retry_interval(self):
        return self._astrill['retry_interval']

    @property
    def username(self):
        return self._astrill['username']

    @property
    def password(self):
        return self._astrill['password']


class Email(Default):
    def __init__(self):
        Default.__init__(self)
        self._email = self._config['EMAIL']

    @property
    def from_addr(self):
        return self._email['from']

    @property
    def to_addr(self):
        return self._email['to']

    @property
    def server(self):
        return self._email['smtp_server']

    @property
    def header(self):
        return self._email['header']

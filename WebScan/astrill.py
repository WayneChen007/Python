# -*- coding: utf-8 -*-
from time import sleep

from pywinauto import application
from pywinauto.application import ProcessNotFoundError
from pywinauto.base_wrapper import ElementNotEnabled
from pywinauto.findbestmatch import MatchError

from initial import Default, AstrillInitial


class Astrill(object):
    """Astrill basic control functions"""

    def __init__(self):
        self.initial = AstrillInitial()
        self.default = Default()
        self._app = application.Application()
        try:
            self._app.connect(path=self.initial.path)
        except ProcessNotFoundError:
            self.start_up()

    def _waiting(self, second):
        sleep(second)

    def start_up(self):
        self._app.start(cmd_line=self.initial.cmd_line)
        self._waiting(10)

    def login(self):
        try:
            self._app['Astrill']['Edit2'].TypeKeys(self.initial.username)
            self._app['Astrill']['CheckBox2'].Click()
            self._app['Astrill']['Edit1'].TypeKeys(self.initial.password)
            self._app['Astrill']['Edit1'].TypeKeys('{ENTER}')
        except ElementNotEnabled:
            self._waiting(5)
            print('Astrill加载超时, 正在重试')
            self.login()
        self._waiting(10)

    def activate(self):
        self._app['Astrill'].click()

    def open_web(self):
        try:
            self._app.connect(path=self.initial.path)
        except ProcessNotFoundError:
            self.start_up()
        self._app['Astrill'].click()
        self._app['Astrill'].ClickInput(coords=(170, 15))
        self._app['PopupMenu'].MenuItem('OpenWeb').ClickInput()

    def turn_on(self):
        if self._app['Astrill']['ON'].exists():
            pass
        else:
            self._app['Astrill']['OFF'].Click()

    def turn_off(self):
        if self._app['Astrill']['OFF'].exists():
            pass
        else:
            self._app['Astrill']['ON'].Click()

    def default_ip_switch(self):
        try:
            self._app.connect(path=self.initial.path)
        except ProcessNotFoundError:
            self.start_up()
        self._app['Astrill'].click()
        self._app['Astrill'].right_click()
        self._waiting(1)
        default_area = self.default.default_vpn.split(',')[0]
        self._app['PopupMenu'].MenuItem(default_area).ClickInput()
        self._waiting(2)
        default_ip = self.default.default_vpn.split(',')[1]
        self._app['PopupMenu'].MenuItem(default_ip).ClickInput()
        self._waiting(1)
        if self._app['PopupMenu'].exists():
            print('默认VPN切换失败, 请检查Config.ini文件!')
        else:
            print('切换至默认VPN...')

    def ip_switch(self, area, ip):
        self._app['Astrill'].right_click()
        self._waiting(0.5)
        self._app['PopupMenu'].MenuItem(area).ClickInput()
        self._waiting(0.5)
        try:
            self._app['PopupMenu'].MenuItem(ip).ClickInput()
            self._waiting(0.5)
            if self._app['PopupMenu'].exists():
                print(ip + '切换失败，请调整VPN设置')
                return False
            else:
                pass
        except MatchError:
            print(area + ' 中找不到' + ip + '，请调整VPN设置')
            return False

    def quit(self):
        try:
            self._app.connect(path=self.initial.path)
        except ProcessNotFoundError:
            pass
        else:
            self._app.kill()

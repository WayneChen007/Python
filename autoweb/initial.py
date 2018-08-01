# -*- coding: utf-8 -*-
"""
The purpose of this script is to read the Config file.
You can add some classes in this script, if you add some browser drivers, of course,
the Config file have to be adjusted accordingly.
"""

import configparser
import sys
from os.path import dirname, join, normpath, exists, splitext
from os import makedirs
from sys import path
from shutil import copy


class Default(object):
    __platform = sys.platform

    def __init__(self):
        """Change the parameters in the following "read" command, If you want this script to read
        the Config file for other paths. Of course, all the parameters below have to be changed
        to a unified path. Also, you have to check the path-related settings in the Config file,
        so I sincerely recommend that you do not change the Config file path.
        """
        self.config_name = 'Config.ini'
        _initial_dir = dirname(__file__)
        _package_ini = normpath(join(_initial_dir, self.config_name))
        _execute_dir = path[0]
        _execute_ini = join(_execute_dir, self.config_name)
        if exists(_execute_ini) is False:
            copy(_package_ini, _execute_dir)
        self._package_dir = dirname(_package_ini)
        self._config = configparser.ConfigParser()
        self._config.read(_execute_ini)
        self.argv_ini_path = _execute_ini

    def _join_package_path(self, path_like):
        if path_like[0:7] == 'drivers':
            return join(self._package_dir, path_like)
        else:
            return path_like

    def _exe_path(self, section, option):
        try:
            ini_exe_path = self._config[section][option]
            exe_path = self._join_package_path(ini_exe_path)
            if self.__platform == 'darwin':
                return splitext(exe_path)[0] if '.exe' in exe_path else exe_path
            elif self.__platform == 'win32':
                return exe_path
        except KeyError:
            return None

    def _log_path(self, section, option):
        try:
            ini_log_path = self._config[section][option]
            log_path = self._join_package_path(ini_log_path)
            log_dir = dirname(log_path)
            if not exists(log_dir):
                makedirs(log_dir)
            return log_path
        except KeyError:
            return None


class Chrome(Default):
    def exe_path(self):
        return self._exe_path('Chrome', 'driver_path')

    def log_path(self):
        return self._log_path('Chrome', 'service_log_path')

    def chrome_proxy(self):
        try:
            _type = self._config['Chrome']['proxy_type']
            _ip = self._config['Chrome']['proxy_ip']
        except KeyError:
            return None
        if _type and _ip:
            _proxy = '--proxy-server=' + _type + '://' + _ip
            return _proxy
        else:
            return None


class PhantomJS(Default):
    def exe_path(self):
        return self._exe_path('PhantomJS', 'phantomJS_path')

    def log_path(self):
        return self._log_path('PhantomJS', 'service_log_path')

    def service_args(self):
        try:
            _service_args = []
            _proxy = '--proxy=' + self._config['PhantomJS']['proxy_ip']
            _type = '--proxy-type=' + self._config['PhantomJS']['proxy_type']
            _service_args.append(_proxy)
            _service_args.append(_type)
            return _service_args
        except KeyError:
            return None


class FireFox(Default):
    def exe_path(self):
        return self._exe_path('FireFox', 'FireFox_path')

    def log_path(self):
        return self._log_path('FireFox', 'service_log_path')

    def proxy_ip(self):
        try:
            _proxy = self._config['FireFox']['proxy_ip']
            return _proxy
        except KeyError:
            return None

    def proxy_type(self):
        try:
            _type = self._config['FireFox']['proxy_type']
            return _type
        except KeyError:
            return None

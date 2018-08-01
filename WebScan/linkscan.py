
#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Wayne Chen
# Version: 2.0.1
"""
The purpose of this program is to scan all the links in the web page,
get the HTTP status code to judge and output the result.

Notes:
    This program is compatible with Python3.6 & autoweb 1.1.0.
    A custom module: autoweb. If you have any comments on this module,
    please contact the author.

Flow Chart:
                        ______________  _________
                       ┃open web side┃← ┥autoweb┃
                        ------┰-------  ---------
                              ↓
                       ┎------┸------┒
                   ----┸----      ---┸-----
                ┏┥ get href┃     ┃ get src ┝┓
                ┃  -----┰---      ----┰---- ┃
                ↑       ↓             ↓     ↑
                ┃  -----┸----    -----┸---- ┃ ---------
                ┗┥check link┃ ┳ ┃check link┝┛←┥profile┃
                 -----------  ┃  -----------  ---------
                              ↓
                         -----┸----      -----------
                        ┃vpn check ┃←————┥pywinauto┃
                         -----┰----      -----------
                              ↓
                        ------┸-----
                        ┃send email┃
                        ------------

Change History:
    Version 2.0.0       2018.01.10
        Reconstruct this script in response to PM requirements.
        Task: http://newicafe.baidu.com:80/issue/hao123-sz-3373/show?from=page
    * Double-thread coordination coroutine decorator.
    * Add the image link scanning.
    * Add request headers -'user-agent'.
    * Won`t switch VPN ip by each website, but use only one ip.
    * More independently function structure.

    Version 2.0.1       2018.01.17
    * Make the code more concise and standardized
    * Support whitelist file

    Version 2.0.2       2018.01.18
    * fix some bugs

    Version 2.1.1       2018.01.29
    * Support for "None-proxy" mode of operation
    * White list is set as a variable that can be overridden by the method

    Version 2.1.2       2018.01.31
    * Urllib method supports 'HTTPS' and request headers and proxy
    * Output HTML table data

"""

import requests
from urllib import request
from initial import Requests, Urllib, Default
from CustomLog import CustomLog
#from astrill import Astrill
from autoweb import Action, sleep, exceptions


class StatusCode(object):
    """HTTP status code"""
    def __init__(self):
        self.requests_ini = Requests()
        self.urllib_ini = Urllib()
        self.logging = CustomLog('logs/')
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,am;q=0.8',
            'Proxy-Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        }

    def requests_code(self, url, proxy, timeout):
        """Use requests to send get requests.
        Some https protocols cause an SSL certificate error.
        :arg url: target url
        :arg proxy: bool
        :arg timeout: int
        :return status code"""
        proxies = self.requests_ini.proxies
        try:
            stat = requests.get(url, headers=self.headers, timeout=timeout,
                                allow_redirects=self.requests_ini.allow_redirects,
                                proxies=proxies).status_code if proxy and proxies is not None else \
                requests.get(url, headers=self.headers, timeout=timeout,
                             allow_redirects=self.requests_ini.allow_redirects).status_code
            return stat
        except BaseException as be:
            return be.__class__.__name__

    def urlopen_code(self, url, proxy):
        """Use urllib to send get requests.
        :arg url: link
        :arg proxy: True or False
        :return status code"""
        proxy_host = self.urllib_ini.proxy_host
        proxy_type = self.urllib_ini.proxy_type
        request._have_ssl = True        # SSL certificate available
        req = request.Request(url, headers=self.headers, method='GET')
        if proxy and proxy_host is not None and proxy_type is not None:
            req.set_proxy(host=proxy_host, type=proxy_type)
        try:
            stat = request.urlopen(req, timeout=self.urllib_ini.timeout).code
            return stat
        except BaseException as be:
            return be.__class__.__name__

    def check_and_format(self, link, proxy):
        """Status code classification, and return log format
        :arg link
        :arg proxy: bool
        :return status format"""
        # urllib request if urllib
        stat = self.urlopen_code(link, proxy)
        print(stat)
        if stat == 200:
            return stat
        # requests first request
        stat = self.requests_code(link, proxy, self.requests_ini.timeout)
        print(stat)
        if stat == 200:
            return stat
        elif stat == 'ReadTimeout':
            # requests longtime request for ReadTimeout
            sleep(1)
            stat = self.requests_code(link, proxy, 20)
        print('link: %s------>>>>%s' % (link, stat))
        return stat if stat == 200 else ('<Response [%s]> %s' % (stat, link) if str(stat).isdigit() else '<%s> %s' % (stat, link))

    def corporations_check(self, func):
        """Associate decorator
        :arg func
        :return inner"""
        def inner(inner_self, *args):
            n = None
            f = func(inner_self, *args)
            while True:
                try:
                    link = f.send(n)
                except StopIteration:
                    break
                n = 1 if n is None else n + 1
                # script here↓
                if link is None:
                    continue
                out_put = self.check_and_format(link, proxy=True)
                if out_put != 200:
                    self.logging.log_output(out_put)
                # script here↑
            f.close()
            return
        return inner


class Spider(object):
    """Web Spider"""
    def __init__(self, url):
        self.driver = Action('Chrome')
        self.driver.headless_mode(False)
        self.driver.load_images(False)
        self.url = url
        self.status_code = StatusCode()
        self.logging = CustomLog('logs/')
        self.load_page()
        self.white_list = []

    def load_page(self):
        """Completely load a page"""
        self.driver.set_page_load_timeout(Default().loading_timeout)
        self.logging.log_output('[INFO] Start scanning  url= %s' % self.url)
        try:
            self.driver.open_url(self.url)
            self.driver.scroll_to_bottom()
        except exceptions.TimeoutException:
            self.driver.stop_loading()
        sleep(10)

    def link_filter(self, link):
        """Filter whitelisted sites
        return False if link in white list else True
        :arg link
        :return bool"""
        return False if link is None or link == self.url + '#' or 'http' not in link or link in self.white_list else True

    def get_tags(self, tag_name):
        """Get the tag elements
        :arg tag_name, HTML tag name
        :return tag_list"""
        tag_list = self.driver.find_tags(tag_name)
        total = len(tag_list)
        self.logging.log_output('[INFO] 找到%sTAG数: %i个' % (tag_name, total)) if total != 0 \
            else self.logging.log_output('[WARNING] 找到0个链接，请检查网络和目标站点')
        return tag_list

    d = StatusCode()

    @d.corporations_check
    def get_links(self, tag_list, attribute):
        """Yield the element's attributes from each tag element
        :arg tag_list, it can be obtained from self.get_tags(*args)
        :arg attribute, the attribute name of the page element"""
        for a_tag in tag_list:
            try:
                attr = a_tag.get_attribute(attribute)
            except exceptions.StaleElementReferenceException:
                self.logging.log_output('[WARNING] ' + '动态隐藏元素: %s' % a_tag)
            yield attr if self.link_filter(attr) else None

    def exit_browser(self):
        """End the drive and output a ending log"""
        self.driver.exit_browser()
        self.logging.log_output('[INFO] End scanning')


class VPNCheck(object):
    """The second round of scanning, open Astrill VPN scanning mode.
    After version2.0, the VPN ip will not be switch for each site,
    but to use a unique ip."""
    def __init__(self):
        self.log_path = StatusCode().logging.log_path
        self.status_code = StatusCode()

    @staticmethod
    def astrill_switch(switch='on'):
        """Astrill switch function
        :arg switch, 'on' or 'off'"""
        from pywinauto.findbestmatch import MatchError
        a = Astrill()
        if switch == 'on':
            try:
                a.login()
            except MatchError:
                pass
            a.open_web(), sleep(2)
            a.turn_on(), sleep(2)
            a.default_ip_switch()
        elif switch == 'off':
            a.quit()
        else:
            print("arg='on' or 'off'")

    def check_from_line(self, line):
        """From the line to find the target link, check and format it as a log form,
        then wrote to result.txt
        :arg line
        :return log form or None"""
        # if object link then check stat.
        if '> http' in line:
            # extract the link
            link = line.split('> ', 1)[1]
            newline = self._vpn_check(link)  # if self.white_list(link, whitelist) else None
        else:
            newline = line if 'url=' in line else None
        return newline

    def _vpn_check(self, link):
        """requests_proxy=False, urllib=True
        :arg link
        :return status code"""
        return self.status_code.check_and_format(link, proxy=False)

    def yield_from_log(self):
        with open(self.log_path, 'r', encoding='utf-8') as ffr:
            while True:
                line = ffr.readline()
                if not line or line is None:
                    break
                line = line.split('] ', 1)[1] if len(line) > 0 else line
                yield line

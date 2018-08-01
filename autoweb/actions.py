#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Wayne Chen
# Version: 1.3.0

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import *
from time import sleep
from .initial import FireFox, Chrome, PhantomJS, Default
import os


class Action(object):
    """
    This 'action' class is used for browser simulation behavior,
    and it encapsulates some common methods that make it easier for
    users to use.

    """
    default_driver = 'Chrome'
    __run_driver = None

    def __init__(self, driver=default_driver):
        """
        from autoweb import Action


            To use the Chrome browser driver:
        a = Action()
            or:
        a = Action('Chrome')    # or all lowercase, such as 'chrome'

            To use the PhantomJS browser driver:
        a = Action('Firefox')    # or all lowercase, such as 'firefox'

            * If you change the location of the config.ini file, you need to adjust
            the parameters in os.system() of 'options' function
        """
        self.__driver_name = driver
        self.chrome_options = webdriver.ChromeOptions()
        self.firefox_profile = webdriver.FirefoxProfile()
        self.firefox_options = Options()
        self.Mouse = Mouse
        self.Keyboard = Keyboard
        self.time_to_wait = None

    def _browser(self):
        _c = Chrome()
        _p = PhantomJS()
        _f = FireFox()

        # add headless setting
        if self.__driver_name in ['Chrome', 'chrome']:
            # argument can not be null
            if _c.chrome_proxy() is not None:
                self.chrome_options.add_argument(_c.chrome_proxy())
            return webdriver.Chrome(executable_path=_c.exe_path(), chrome_options=self.chrome_options, service_log_path=_c.log_path())

        elif self.__driver_name in ['FireFox', 'firefox', 'Firefox']:
            if _f.proxy_ip() is not None:
                webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
                    "httpProxy": _f.proxy_ip(),
                    "ftpProxy": _f.proxy_ip(),
                    "sslProxy": _f.proxy_ip(),
                    "proxyType": "MANUAL"
                }
            return webdriver.Firefox(executable_path=_f.exe_path(), log_path=_f.log_path(), options=self.firefox_options)

        elif self.__driver_name in ['PhantomJS', 'Phantomjs', 'phantomjs']:
            return webdriver.PhantomJS(executable_path=_p.exe_path(), service_args=_p.service_args(), service_log_path=_p.log_path())
            # To add a browser driver, insert elif here
        else:
            raise AttributeError

    def __argument(self, switch, chrome_op, firefox_op):
        if switch:
            if chrome_op not in self.chrome_options.arguments:
                self.chrome_options.add_argument(chrome_op)
            if firefox_op not in self.firefox_options.arguments:
                self.firefox_options.add_argument(firefox_op)
        elif switch is False:
            try:
                self.chrome_options.arguments.remove(chrome_op)
                self.firefox_options.arguments.remove(firefox_op)
            except ValueError:
                pass
        else:
            raise TypeError

    def set_page_load_timeout(self, time_to_wait):
        """Used to set the page full load time-out, full load that page all
        rendering, asynchronous synchronization scripts are completed."""
        self.time_to_wait = time_to_wait

    def private_mode(self, private=False):
        self.__argument(private, '-incognito', '-private')

    def headless_mode(self, headless=False):
        self.__argument(headless, '--headless', '-headless')

    def load_images(self, load=True):
        if not load:
            __chrome_setting = 2
            __firefox_setting = 2
            __phantomjs_setting = False
        else:
            __chrome_setting = 1
            __firefox_setting = 1
            __phantomjs_setting = True
        self.chrome_options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": __chrome_setting})
        self.firefox_options.set_preference("permissions.default.image", __firefox_setting)
        d_cap = dict(DesiredCapabilities.PHANTOMJS)
        d_cap["phantomjs.page.settings.loadImages"] = __phantomjs_setting

    @staticmethod
    def options():
        """View the configuration file"""
        return os.system(Default().argv_ini_path)

    def open_url(self, url):
        self.__run_driver = self._browser()
        if self.time_to_wait is not None:
            self.__run_driver.set_page_load_timeout(self.time_to_wait)
            self.__run_driver.set_script_timeout(self.time_to_wait)
        self.Mouse = Mouse(self.__run_driver)
        self.Keyboard = Keyboard(self.__run_driver)
        self.__run_driver.get(url)

    def add_extension(self, extension_path):
        """Add Chrome extension"""
        self.chrome_options.add_extension(extension_path)
        self.firefox_profile.add_extension(extension_path)

    def until_element_located(self, time_to_wait, css_locator):
        """Wait for the page to load to complete, find a condition to continue
        after the implementation of the follow-up code, if the set time conditions
        have not occurred, then throw an exception"""
        WebDriverWait(self.__run_driver, time_to_wait).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_locator)))

    def maximize_window(self):
        self.__run_driver.maximize_window()

    def scroll_to_bottom(self):
        self.__run_driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    def stop_loading(self):
        """Stop page loading(phantomJS does not support this command)"""
        self.__run_driver.execute_script('window.stop()')

    def new_tab(self):
        self.__run_driver.execute_script('window.open()')

    def execute_script(self, script):
        return self.__run_driver.execute_script(script)

    def find_element(self, css_selector_or_xpath):
        """
        Finds an elements by css selector or Xpath.
        :param css_selector_or_xpath: css selector or xpath
        :return: web element
        """
        if '/' in css_selector_or_xpath:
            return self.__run_driver.find_element_by_xpath(css_selector_or_xpath)
        elif '/' not in css_selector_or_xpath:
            return self.__run_driver.find_element_by_css_selector(css_selector_or_xpath)

    def find_elements(self, css_selector_or_xpath):
        """
        Finds multiple elements by css selector or Xpath.
        :param css_selector_or_xpath: css selector or xpath
        :return: web elements
        """
        if '/' in css_selector_or_xpath:
            return self.__run_driver.find_elements_by_xpath(css_selector_or_xpath)
        elif '/' not in css_selector_or_xpath:
            return self.__run_driver.find_elements_by_css_selector(css_selector_or_xpath)

    def find_tags(self, tag_name):
        """
        Finds multiple elements by tag name.
        :param tag_name: tag name
        :return: web elements by tag name
        """
        return self.__run_driver.find_elements_by_tag_name(tag_name)

    def find_classes(self, classes):
        """
        Finds multiple elements by class.
        :param classes: class name
        :return: web elements by class name
        """
        return self.__run_driver.find_elements_by_class_name(classes)

    def get_attribute(self, css_selector_or_xpath, attribute):
        """
        Gets the given attribute or property of the element.
        :param css_selector_or_xpath:
        :param attribute: HTML attribute
        :return: value of HTML attribute
        """
        return self.find_element(css_selector_or_xpath).get_attribute(attribute)

    def back(self):
        self.__run_driver.execute('goBack')

    def forward(self):
        self.__run_driver.execute('goForward')

    def refresh(self):
        self.__run_driver.execute('refresh')

    def close_tab(self):
        self.__run_driver.execute('close')

    def close_other_tabs(self, main_handle):
        """Close other tabs except the main tab"""
        for handle in self.__run_driver.window_handles:
            if handle == main_handle:
                continue
            elif handle != main_handle:
                self.__run_driver.execute_script('window.stop()')
                self.__run_driver.switch_to.window(handle)
                self.__run_driver.close()
                self.__run_driver.switch_to.window(main_handle)

    @property
    def page_title(self):
        return self.__run_driver.title

    def tag_name(self, css_selector_or_xpath):
        """
        :param css_selector_or_xpath:
        :return:
        """
        return self.find_element(css_selector_or_xpath).tag_name

    @property
    def page_source(self):
        return self.__run_driver.page_source

    @property
    def current_url(self):
        return self.__run_driver.current_url

    @property
    def current_handle(self):
        return self.__run_driver.current_window_handle

    @property
    def window_handles(self):
        return self.__run_driver.window_handles

    @property
    def switch_to(self):
        return self.__run_driver.switch_to

    def _initialize(self):
        self.__run_driver = None
        self.chrome_options = webdriver.ChromeOptions()
        self.firefox_profile = webdriver.FirefoxProfile()
        self.firefox_options = Options()

    def exit_browser(self):
        """Close the browser engine and initialize."""
        self.__run_driver.quit()

    def is_display(self, css_selector_or_xpath):
        return self.find_element(css_selector_or_xpath).is_displayed()

    def css_property(self, css_selector_or_xpath, css_property):
        """
        The value of a CSS property.
        :param css_selector_or_xpath: css selector or xpath
        :param css_property: HTML property
        :return: value of HTML property
        """
        return self.find_element(css_selector_or_xpath).value_of_css_property(css_property)

    def is_element_exist(self, css_selector_or_xpath):
        """
        Determines whether an element exists and returns a Boolean value.
        :param css_selector_or_xpath:
        :return: bool
        """
        try:
            self.find_element(css_selector_or_xpath)
            return True
        except NoSuchElementException:
            return False

    def get_performance(self):
        """Get the web front end performance through a js directive, which includes
        the time at which various resources are loaded"""
        return self.__run_driver.execute_script('return window.performance.timing')

    def screen_shot(self, path):
        self.__run_driver.get_screenshot_as_file(path)

    def get_cookie(self, name):
        return self.__run_driver.get_cookie(name)

    def get_cookies(self):
        return self.__run_driver.get_cookies()

    def delete_all_cookies(self):
        self.__run_driver.delete_all_cookies()

    def select(self, css_selector_or_xpath):
        """Constructor. A check is made that the given element is, indeed, a SELECT tag. If it is not,
        then an UnexpectedTagNameException is thrown."""
        return Select(self.find_element(css_selector_or_xpath))


class Mouse(object):
    """Mouse action class"""
    def __init__(self, mouse_driver):
        self.__driver = mouse_driver

    def find_element(self, css_selector_or_xpath):
        if '/' in css_selector_or_xpath:
            return self.__driver.find_element_by_xpath(css_selector_or_xpath)
        elif '/' not in css_selector_or_xpath:
            return self.__driver.find_element_by_css_selector(css_selector_or_xpath)

    def click(self, css_selector_or_xpath):
        self.find_element(css_selector_or_xpath).click()

    def hover(self, css_selector_or_xpath):
        ActionChains(self.__driver).move_to_element(self.find_element(css_selector_or_xpath)).perform()

    def double_click(self, css_selector_or_xpath):
        ActionChains(self.__driver).double_click(self.find_element(css_selector_or_xpath)).perform()

    def right_click(self, css_selector_or_xpath):
        ActionChains(self.__driver).context_click(self.find_element(css_selector_or_xpath)).perform()

    def drag(self, draggable, target):
        """Drag a dragable element to the target element position, and if it can not be dragged,
        it will not do anything and will not throw any errors"""
        __s = self.find_element(draggable)
        __t = self.find_element(target)
        ActionChains(self.__driver).click_and_hold(__s).release(__t).perform()


class Keyboard(object):
    """Keyboard action class"""
    def __init__(self, keyboard_driver):
        self.keyboard_driver = keyboard_driver

    def find_element(self, css_selector_or_xpath):
        if '/' in css_selector_or_xpath:
            return self.keyboard_driver.find_element_by_xpath(css_selector_or_xpath)
        elif '/' not in css_selector_or_xpath:
            return self.keyboard_driver.find_element_by_css_selector(css_selector_or_xpath)

    def key_input(self, css_selector_or_xpath, value):
        self.find_element(css_selector_or_xpath).send_keys(value)

    def key_press(self, keys, times=1):
        """Analog keypad action, almost all keys are supported, the first parameter
        can refer to the 'Keys' command, such as 'Keys.ENTER', which can be simulated
        by pressing the Enter key, the second parameter is the number of loops, the
        default is 0.5 second"""
        for t in range(times):
            ActionChains(self.keyboard_driver).send_keys(keys).perform()
            sleep(0.5)

    def hold_and_press(self, hold_key, press_key, times=1):
        """Press and hold one key and the other key for loop operation, The first parameter
        is the 'hold-key', and the second parameter is the key for the loop operation, and
        when the loop ends, loosen the first key, third parameter is the number of loops,
        the default is 0.5 second"""
        ActionChains(self.keyboard_driver).key_down(hold_key).perform()
        for t in range(times):
            ActionChains(self.keyboard_driver).send_keys(press_key).perform()
            sleep(0.5)
        ActionChains(self.keyboard_driver).key_up(hold_key).perform()

    def submit(self, css_selector_or_xpath):
        self.find_element(css_selector_or_xpath).submit()

    def clear(self, css_selector_or_xpath):
        self.find_element(css_selector_or_xpath).clear()

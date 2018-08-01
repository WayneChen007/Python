Autoweb

Notes:
    This program is compatible with Python3.6 & Selenium3.8.1
    Supports three browser drivers: Chrome(default driver), Firefox and PhantomJS(with out interface)
    The root directory has the configuration file "config.ini", which can be set to the
    driver's execution directory, web proxy, etc.

Example:

    from autoweb import Action, exceptions


    Action().options()   # To adjust the configuration file
    a = Action()
    a.open_url('http://www.baidu.com')
    a.Mouse.click('#u1 > a:nth-child(1)')
    a.Keyboard.key_input('#kw', 'news')
    a.Keyboard.submit('#kw')
    sleep(5)
    try:
        #To use the selenium method:
        a.driver.find_element_by_xpath('//*[@id="1"]/h3/a/em').text
        #To use exceptions:
    except exceptions.NoSuchElementException as s:
        raise s
    a.exit_browser()

Change History:

    Version 1.0.2       2017.9.14
    * Identify lowercase parameters.
    * Support with the command to open the Config file, one-click installation.
    * Added some necessary annotations.

    Version 1.0.3       2017.9.15
    * New function: Action().tag_name(self, css_selector_or_xpath).
    * New function: Keyboard().hold_and_press(self, hold_key, press_key, times=1).

    Version 1.0.4       2017.10.19
    * Use the staticmethod and inheritance to optimize part of the initial code.
    * Fixed Chrome's proxy method.

    Version 1.1.0       2017.12.23
    * Support for independent configuration files.

    Version 1.1.1       2018.1.11
    * Fix some bugs.

    Version 1.2.1       2018.1.30
    * Support for None-images loading and headless mode.
    * Will not run the driver in init.
    * Update selenium to 3.8.1.
    * Update ChromeDriver to 2.35.
    * External ChromeOptions, allows users to customize the configuration.

    Version 1.2.2        2018.1.31
    * Support FireFox browser.
    * External firefox profile and options, allows users to customize the configuration.

    Version 1.2.3       2018.2.5
    * Support private mode and add extension for Chrome and Firefox.
    * Delete the configuration item, if switch is False.

    Version 1.3.0       2018.2.7
    * Support for iOS.
    * Optimized file structure
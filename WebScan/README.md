WebScan

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
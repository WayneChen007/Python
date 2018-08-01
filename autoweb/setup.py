"""
The purpose of this script is to install the webframe module.
This script is not part of the webframe module and will not be installed
into the Python module library.
If you have multiple versions of Python, the webframe module will be
installed in the Python version where the script is executed.
If there is a problem with this installation, please contact us.
"""

import os
import shutil
import sys


if __name__ == '__main__':
    path = sys.path[0]
    builtin_path = os.path.dirname(shutil.__file__)
    autoweb_path = os.path.join(builtin_path, 'site-packages/autoweb')
    if not os.path.exists(autoweb_path):
        os.mkdir(autoweb_path)
    shutil.rmtree(autoweb_path, True)
    shutil.copytree(path, autoweb_path)
    if sys.platform == 'darwin':
        os.system('open -a TextEdit ' + os.path.join(autoweb_path, 'Config.ini'))
    elif sys.platform == 'win32':
        os.system(os.path.join(autoweb_path, 'Config.ini'))

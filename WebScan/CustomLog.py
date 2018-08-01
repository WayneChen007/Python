import time
import os
import sys


class CustomLog(object):
    """Output logs with custom style"""

    def __init__(self, path, ):
        self.date_time = time.strftime("%Y-%m-%d", time.localtime())
        self.path = os.path.join(str(sys.path[0]), str(path))
        self.log_path = self.path + self.date_time + '.log'
        self.mk_dir()

    @property
    def log_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def mk_dir(self):
        dir_path = os.path.dirname(self.path)
        if os.path.exists(dir_path) is False:
            os.makedirs(dir_path)

    def log_output(self, content):
        log_file = open(self.log_path, 'a+', encoding='utf-8')
        self.date_time = time.strftime("%Y-%m-%d", time.localtime())
        log_file.write("[%s] %s\n" % (self.log_time, content))
        log_file.close()

    def log_without_time(self, content):
        log_file = open(self.log_path, 'a+', encoding='utf-8')
        log_file.write("[%s] %s\n" % content)
        log_file.close()

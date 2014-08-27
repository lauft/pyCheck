__author__ = 'lauft'

import os
from stat import *


class CheckPath(object):
    """
    check whether a path meets certain requirements
    """

    def __init__(self, path):
        self.path = path

    def does_exist(self):
        """

        :rtype : bool
        """
        return os.path.exists(self.path)

    def does_not_exist(self):
        return not self.does_exist()

    def is_a_file(self):
        return os.path.isfile(self.path)

    def is_not_a_file(self):
        return not self.is_a_file()
    
    def is_a_directory(self):
        return os.path.isdir(self.path)
    
    def is_not_a_directory(self):
        return not self.is_a_directory()

    def is_an_executable(self):
        if self.is_not_a_file():
            return False
        return os.stat(self.path).st_mode & S_IXUSR

    def has_permissions(self, mode):
        return S_IMODE(os.stat(self.path).st_mode) == mode

    def does_contain(self, item):
        path = os.path.join(self.path, item)
        return os.path.exists(path)

    def does_not_contain(self, item):
        return not self.does_contain(item)
__author__ = 'lauft'

import os


class CheckPath():
    """check whether a path meets certain requirements"""

    def __init__(self, path):
        self.path = path

    def does_exist(self):
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
        mode = os.stat(self.path).st_mode
        return (mode == 777) #& self.is_a_file()
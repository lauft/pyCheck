__author__ = 'lauft'

import os


class CheckPath():
    """check whether a path meets certain requirements"""

    def __init__(self):
        """


        """

    def does_exist(self, path):
        """

        :param path:
        """
        return os.path.exists(path)

    def does_not_exist(self, path):
        return not self.does_exist(path)

    def is_a_file(self, path):
        return os.path.isfile(path)

    def is_not_a_file(self, path):
        return not self.is_a_file(path)
    
    def is_a_directory(self, path):
        """

        :rtype : bool
        """
        result = os.path.isdir(path)
        return result
    
    def is_not_a_directory(self, path):
        return not self.is_a_directory(path)

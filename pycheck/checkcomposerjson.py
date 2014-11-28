import json
import pycheck.checkjson

__author__ = 'lauft'


class CheckComposerJson(pycheck.checkjson.CheckJson):
    """
    check whether a composer JSON file meets certain requirements
    """
    def __init__(self, path):
        pycheck.checkjson.CheckJson.__init__(self, path)

        if not self.does_contain_member("name"):
            self.failed = True

        if not self.does_contain_member("version"):
            self.failed = True

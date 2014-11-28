import json

__author__ = 'lauft'


class CheckJson():
    """
    check whether a composer JSON file meets certain requirements
    """
    def __init__(self, path):
        self.failed = False

        try:
            composer = open(path)
            self.json = json.load(composer)
            composer.close()
        except:
            print 'error when opening "' + path + '"'
            self.failed = True

    def does_contain_member(self, member):
        if self.failed:
            return False

        if member not in self.json:
            print 'no key "' + member + '"'
            return False

        return True

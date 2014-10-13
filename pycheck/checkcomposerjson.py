import json

__author__ = 'lauft'


class CheckComposerJson():
    """
    check whether a composer JSON file meets certain requirements
    """
    def __init__(self, path):
        self.failed = False

        try:
            composer = open(path)
            self.json_text = json.load(composer)
            composer.close()
        except:
            print 'error when opening "' + path + '"'
            self.failed = True

    def does_contain_member(self, member):
        if self.failed:
            return False

        if member not in self.json_text:
            #print 'no key "' + key + '" :[' + self.path + ']'
            return False

        return True

    #def array_at(self, index):

#
#        if 'support' in self.data:
#            if 'wiki' not in self.data['support']:
#                print 'no wiki in support (' + self.path + ')'
#                success = False
#                if 'source' not in self.data['support']:
#                    print 'no source in support (' + self.path + ')'
#                success = False
#            if 'issues' not in self.data['support']:
#                print 'no issuses in support (' + self.path + ')'
#                success = False
#        else:
#            print 'no support (' + self.path + ')'
#            success = False
#
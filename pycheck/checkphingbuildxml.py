__author__ = 'lauft'


class CheckPhingBuildXml():
    """
    check whether a phing build XML file meets certain requirements
    """

    def __init__(self, path='build.xml'):
        self.path = path


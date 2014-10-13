__author__ = 'lauft'

import unittest
import os
import pycheck.checkcomposerjson


class CheckComposerJsonFileTestCase(unittest.TestCase):
    """CheckJsonFile test case"""

    def setUp(self):
        """

        :return:
        """
        self.validTestFile = "valid_composer.json"
        self.invalidTestFile = "path/to/invalid/testFile"

    def tearDown(self):
        """

        :return:
        """

    #def test_file_validation(self):
    #    """
    #    test file validation
    #    :return:
    #    """
    #    self.assertTrue(pycheck.checkcomposerjson.CheckComposerJson(self.validTestFile).is_valid())
    #    self.assertFalse(pycheck.checkcomposerjson.CheckComposerJson(self.invalidTestFile).is_valid())

    #def test_existing_requirement_is_found(self):
    #    """
    #
    #    :return:
    #    """
    #    self.assertTrue(pycheck.checkcomposerjson.CheckComposerJson(self.validTestFile).has_requirement(self.existingRequirement))

    def test_has_key(self):
        """

        :return:
        """
        self.assertTrue(pycheck.checkcomposerjson.CheckComposerJson(self.validTestFile).does_contain_member('support'))
        self.assertFalse(pycheck.checkcomposerjson.CheckComposerJson(self.validTestFile).does_contain_member('foo'))

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
        self.validTestFile = "path/to/valid/testFile"
        self.invalidTestFile = "path/to/invalid/testFile"

    def tearDown(self):
        """

        :return:
        """

    def test_file_validation(self):
        """
        test file validation
        :return:
        """
        self.assertTrue(pycheck.checkcomposerjson.CheckComposerJson(self.validTestFile).is_valid())
        self.assertFalse(pycheck.checkcomposerjson.CheckComposerJson(self.invalidTestFile).is_valid())

    def test_existing_requirement_is_found(self):
        """

        :return:
        """
        self.assertTrue(pycheck.checkcomposerjson.CheckComposerJson(self.validTestFile).has_requirement(self.existingRequirement))
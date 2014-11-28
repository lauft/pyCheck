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
        self.invalidTestFile = "invalid_composer.json"
        self.testFileEmptyArray = "empty_array.json"
        self.testFileArray = "array.json"
        self.testFileEmptyObject = "empty_object.json"
        self.testFileObject = "object.json"
        self.nonExistentFile = "this/path/does/not/exist"

    def tearDown(self):
        """

        :return:
        """

    def test_fails_on_invalid_path(self):
        """

        :return:
        """
        self.assertTrue(pycheck.checkcomposerjson.CheckComposerJson(self.nonExistentFile).failed)

    def test_fails_on_invalid_file(self):
        """

        :return:
        """
        self.assertTrue(pycheck.checkcomposerjson.CheckComposerJson(self.invalidTestFile).failed)

    def test_fails_on_empty_array(self):
        """
        A file with an empty array is a valid JSON file but an invalid composer file

        :return:
        """
        self.assertTrue(pycheck.checkcomposerjson.CheckComposerJson(self.testFileEmptyArray).failed)

    def test_fails_on_array(self):
        """
        A file with an array is valid JSON file but an invalid composer file

        :return:
        """
        self.assertTrue(pycheck.checkcomposerjson.CheckComposerJson(self.testFileArray).failed)

    def test_fails_on_emtpy_object(self):
        """
        A file with an empty object is a valid JSON file but an invalid composer file

        :return:
        """
        self.assertTrue(pycheck.checkcomposerjson.CheckComposerJson(self.testFileEmptyObject).failed)

    def test_fails_on_non_composer_object(self):
        """
        A composer file contains an object with a set of minimal required keys

        :return:
        """
        self.assertTrue(pycheck.checkcomposerjson.CheckComposerJson(self.testFileObject).failed)

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

    def test_contains_member(self):
        """

        :return:
        """
        self.assertTrue(pycheck.checkcomposerjson.CheckComposerJson(self.validTestFile).does_contain_member('name'))
        self.assertFalse(pycheck.checkcomposerjson.CheckComposerJson(self.validTestFile).does_contain_member('foo'))

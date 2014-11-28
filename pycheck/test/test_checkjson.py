__author__ = 'lauft'

import unittest
import os
import pycheck.checkjson


class CheckJsonFileTestCase(unittest.TestCase):
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
        self.assertTrue(pycheck.checkjson.CheckJson(self.nonExistentFile).failed)

    def test_fails_on_invalid_file(self):
        """

        :return:
        """
        self.assertTrue(pycheck.checkjson.CheckJson(self.invalidTestFile).failed)

    def test_passes_on_empty_array(self):
        """
        A file with an empty array is a valid JSON file

        :return:
        """
        self.assertFalse(pycheck.checkjson.CheckJson(self.testFileEmptyArray).failed)

    def test_passes_on_array(self):
        """
        A file with an array is valid JSON file

        :return:
        """
        self.assertFalse(pycheck.checkjson.CheckJson(self.testFileArray).failed)

    def test_passes_on_emtpy_object(self):
        """
        A file with an empty object is a valid JSON file

        :return:
        """
        self.assertFalse(pycheck.checkjson.CheckJson(self.testFileEmptyObject).failed)

    def test_passes_on_object(self):
        """
        A file with an object is a valid JSON file

        :return:
        """
        self.assertFalse(pycheck.checkjson.CheckJson(self.testFileObject).failed)

    def test_does_contain_member(self):
        """
        A member is a name/value pair within a JSON object
        :return:
        """
        self.assertTrue(pycheck.checkjson.CheckJson(self.testFileObject).does_contain_member(''))
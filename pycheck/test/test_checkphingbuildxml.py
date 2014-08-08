__author__ = 'lauft'

import unittest
import os
import pycheck.checkphingbuildxml


class CheckPhingBuildXmlTestCase(unittest.TestCase):
    """CheckJsonFile test case"""

    def setUp(self):
        """
        :return:
        """
        self.testFile = "path/to/testfile"
        self.existingTarget = "existing"
        self.missingTarget = "missing"

    def tearDown(self):
        """
        :return:
        """

    def test_existing_phing_target_is_detected(self):
        """
        existing phing target is detected
        :return:
        """
        self.assertTrue(pycheck.checkphingbuildxml.CheckPhingBuildXml(self.testFile).has_target(self.existingTarget))
        self.assertFalse(pycheck.checkphingbuildxml.CheckPhingBuildXml(self.testFile).has_not_target(self.existingTarget))

    def test_missing_phing_target_is_detected(self):
        """
        missing phing target is detected
        :return:
        """
        self.assertTrue(pycheck.checkphingbuildxml.CheckPhingBuildXml(self.testFile).has_not_target(self.missingTarget))
        self.assertFalse(pycheck.checkphingbuildxml.CheckPhingBuildXml(self.testFile).has_target(self.missingTarget))

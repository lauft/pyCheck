__author__ = 'lauft'

import unittest
import os
import pycheck.checkpath


class CheckPathTestCase(unittest.TestCase):
    """Sample test case"""

    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print "FooTest:setUp_:begin"
        ## do something...
        self.classUnderTest = pycheck.checkpath.CheckPath()
        os.makedirs("tmp", 0755)
        os.makedirs("tmp/foo")
        open("tmp/bar", "a")
        print "FooTest:setUp_:end"

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print "FooTest:tearDown_:begin"
        ## do something...
        os.remove('tmp/bar')
        os.removedirs('tmp/foo')
        print "FooTest:tearDown_:end"

    def test_existing_file_is_found(self):
        """existing file is found"""
        self.assertTrue(self.classUnderTest.does_exist("tmp/bar"), "did not find existing file")
        print "FooTest:testA"

    def test_missing_file_is_detected(self):
        """missing file is detected"""
        self.assertFalse(self.classUnderTest.does_exist("tmp/baz"), "did not detect missing file")
        print "FooTest:testB"

    def test_non_existing_file_is_confirmed(self):
        """non existing file is confirmed"""
        self.assertTrue(self.classUnderTest.does_not_exist("tmp/baz"), "did not confirm a non-existing file")

    def test_existing_file_is_not_overlooked(self):
        """existing file is not overlooked"""
        self.assertFalse(self.classUnderTest.does_not_exist("tmp/bar"), "did overlook an existing file")

    def test_file_is_detected_as_file(self):
        self.assertTrue(self.classUnderTest.is_a_file("tmp/bar"), "did not detect 'bar' as a file")

    def test_directory_does_not_pass_as_file(self):
        self.assertFalse(self.classUnderTest.is_a_file("tmp/foo"), "did confuse directory 'tmp/foo' with file")

    def test_directory_is_detected_as_directory(self):
        self.assertTrue(self.classUnderTest.is_a_directory("tmp/foo"), "did not detect 'foo' as directory")

    def test_file_does_not_pass_as_directory(self):
        self.assertFalse(self.classUnderTest.is_a_directory("tmp/bar"), "did confuse file 'tmp/bar' with directory")
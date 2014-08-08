__author__ = 'lauft'

import unittest
import os
import pycheck.checkpath


class CheckPathTestCase(unittest.TestCase):
    """Checkpath test case"""

    def setUp(self):
        """ Setting up for the test """
        os.makedirs("tmp", 0755)
        os.makedirs("tmp/foo")
        open("tmp/bar", "a")
        os.chmod("tmp/bar", 0644)
        open("tmp/exe", "a")
        os.chmod("tmp/exe", 0700)

    def tearDown(self):
        """Cleaning up after the test"""
        os.remove('tmp/bar')
        os.remove('tmp/exe')
        os.removedirs('tmp/foo')

    def test_existing_file_is_found(self):
        """existing file is found"""
        self.assertTrue(pycheck.checkpath.CheckPath("tmp/bar").does_exist(), "did not find existing file")
        self.assertFalse(pycheck.checkpath.CheckPath("tmp/bar").does_not_exist(), "did not find existing file")

    def test_missing_file_is_detected(self):
        """missing file is detected"""
        self.assertFalse(pycheck.checkpath.CheckPath("tmp/baz").does_exist(), "did not detect missing file")
        self.assertTrue(pycheck.checkpath.CheckPath("tmp/baz").does_not_exist(), "did not detect missing file")

    def test_non_existing_file_is_confirmed(self):
        """non existing file is confirmed"""
        self.assertTrue(pycheck.checkpath.CheckPath("tmp/baz").does_not_exist(), "did not confirm a non-existing file")
        self.assertFalse(pycheck.checkpath.CheckPath("tmp/baz").does_exist(), "did not confirm a non-existing file")

    def test_existing_file_is_not_overlooked(self):
        """existing file is not overlooked"""
        self.assertFalse(pycheck.checkpath.CheckPath("tmp/bar").does_not_exist(), "did overlook an existing file")
        self.assertTrue(pycheck.checkpath.CheckPath("tmp/bar").does_exist(), "did overlook an existing file")

    def test_file_is_detected_as_file(self):
        """file is detected as type file"""
        self.assertTrue(pycheck.checkpath.CheckPath("tmp/bar").is_a_file(), "did not detect 'bar' as a file")
        self.assertFalse(pycheck.checkpath.CheckPath("tmp/bar").is_not_a_file(), "did not detect 'bar' as a file")

    def test_directory_does_not_pass_as_file(self):
        """directory is not confused with file"""
        self.assertFalse(pycheck.checkpath.CheckPath("tmp/foo").is_a_file(), "confused directory 'tmp/foo' with file")
        self.assertTrue(pycheck.checkpath.CheckPath("tmp/foo").is_not_a_file(), "confused directory 'tmp/foo' with file")

    def test_directory_is_detected_as_directory(self):
        """directory is detected as type directory"""
        self.assertTrue(pycheck.checkpath.CheckPath("tmp/foo").is_a_directory(), "did not detect 'foo' as directory")
        self.assertFalse(pycheck.checkpath.CheckPath("tmp/foo").is_not_a_directory(), "did not detect 'foo' as directory")

    def test_file_does_not_pass_as_directory(self):
        """file is not confused with directory"""
        self.assertFalse(pycheck.checkpath.CheckPath("tmp/bar").is_a_directory(), "confused file 'tmp/bar' with directory")
        self.assertTrue(pycheck.checkpath.CheckPath("tmp/bar").is_not_a_directory(), "confused file 'tmp/bar' with directory")

    def test_executable_is_detected(self):
        """executeable is deteced"""
        self.assertTrue(pycheck.checkpath.CheckPath("tmp/exe").is_an_executable(), "did not identify 'exe' as an executable")

    def test_directory_does_not_pass_as_executeable(self):
        """directory is not confused with executable"""
        self.assertFalse(pycheck.checkpath.CheckPath("tmp/foo").is_an_executable(), "confused directory 'tmp/foo' with executable")

    def test_permission_bits_are_identified(self):
        """permission bits are identified"""
        self.assertTrue(pycheck.checkpath.CheckPath("tmp").has_permissions(0755), "did not identify permissions for 'tmp'")
        self.assertTrue(pycheck.checkpath.CheckPath("tmp/foo").has_permissions(0775), "did not identify permissions for 'tmp/foo'")
        self.assertTrue(pycheck.checkpath.CheckPath("tmp/bar").has_permissions(0644), "did not identify permissions for 'tmp/bar'")
        self.assertTrue(pycheck.checkpath.CheckPath("tmp/exe").has_permissions(0700), "did not identify permissions for 'tmp/exe'")
        self.assertFalse(pycheck.checkpath.CheckPath("tmp/exe").has_permissions(0644), "did not identify permissions for 'tmp/exe'")

import sys
import unittest

class TestSample(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(42, 42)

# def test_python_version():
#     assert sys.version_info_major == 3, f"Expected major version 3, but got {sys.version_info.major}"
#     assert sys.version_info_minor >= 11, f"Expected minor version 11, but got {sys.version_info.minor}"

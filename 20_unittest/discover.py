"""
    Discover tests for unittest of Python.

    Usage:
        python -m unittest discover -s test -p "test_*.py"
        python -m unittest discover test "test_*.py"

        or

        python discover.py
"""
import unittest

def suite():
    test_suite = unittest.TestSuite()
    all_test_suite = unittest.defaultTestLoader.discover("test", pattern="test_*.py")
    for ts in all_test_suite:
        test_suite.addTest(ts)
    return test_suite

if __name__ == "__main__":
    mySuite = suite()
    unittest.TextTestRunner().run(mySuite)

"""
    Sample of unittest for Python.

    ref:
        http://docs.python.jp/3/library/unittest.html
        http://stackoverflow.com/questions/12011091/trying-to-implement-python-testsuite
        http://stackoverflow.com/questions/1732438/how-to-run-all-python-unit-tests-in-a-directory

    how to execute:
        pattern1: $ python -m unittest unittest_sample.py
        pattern2: $ python unittest_sample.py
"""
import unittest

# @unittest.skip("Skip test class sample")
class MyTest(unittest.TestCase):

    def setUp(self):
        print("setUp is called.")

    def tearDown(self):
        print("tearDown is called.")

    @classmethod
    def setUpClass(cls):
        print("setUpClass is called.")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass is called.")

    def test_do_something(self):
        print("test_do_something")
        one = 1
        self.assertEqual(one, 1, "one is 1")

    def test_do_otherthing(self):
        print("test_do_otherthing")
        two = 2
        self.assertTrue(two == 2, "two is 2")

    @unittest.skip("Skip Test Sample")
    def test_do_thing_for_skip(self):
        print("skip this method, so it is never called.")

if __name__ == "__main__":
    unittest.main()
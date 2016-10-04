import unittest

class MyTest(unittest.TestCase):

    def test_mytest_01(self):
        print("test_mytest_01 is called")
        one = 1
        self.assertEqual(one, 1, "one is 1")
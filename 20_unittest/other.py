import unittest

class OtherTest(unittest.TestCase):

    def test_other_01(self):
        print("test_other_01 is called")
        two = 2
        self.assertEqual(two, 2, "two is 2")
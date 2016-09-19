import unittest
from get_one import get_one

class SubSub1Test(unittest.TestCase):

    def test_subsub1_01(self):
        print("test_subsub1_01 is called")
        self.assertEqual(get_one(), 1, "get_one() must return 1")
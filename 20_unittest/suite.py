import unittest
import test
import other

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(test.MyTest))
    test_suite.addTest(unittest.makeSuite(other.OtherTest))
    return test_suite

if __name__ == "__main__":
    mySuite = suite()
    unittest.TextTestRunner().run(mySuite)

import unittest
import mytest
import other

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(mytest.MyTest))
    test_suite.addTest(unittest.makeSuite(other.OtherTest))
    return test_suite

if __name__ == "__main__":
    mySuite = suite()
    unittest.TextTestRunner().run(mySuite)

#encoding=utf-8

import unittest


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'class setup'

    @classmethod
    def tearDownClass(cls):
        print 'class teardown'

    def setUp(self):
        print 'setup'

    def tearDown(self):
        print 'teardown'

    def test_1(self):
        print 'test 1'

    def test_2(self):
        print 'test 2'


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

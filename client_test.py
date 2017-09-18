import unittest
import xmlrunner
import RandomNameFromListServer
import os
import urllib2

class TestClient(unittest.TestCase):

    def setUp(self):
        pass

    def testGet(self):
        url = os.environ['TEST_URL']
        print "URL: " + url
        test_text = '{"names":["Thomas, John P.","Gregory, Lucas A.","Samuels, Karl","Coen, Peter","Cohen, Greg","Douglass, Cathy R.","Gifford, Charles C.","Bassar, Ahmed H.","Hanson-Gretel, Andrew M."]}\r\n'
        for i in range(0,20):
            response = urllib2.urlopen(url=url, data=test_text).read().splitlines()
            name = response[-1]
            self.assertRegexpMatches(name,"^\"[A-Za-z\-]+, [A-Za-z\-]+( \w\.){0,1}\"$")

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

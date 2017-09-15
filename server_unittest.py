import unittest
import xmlrunner
import RandomNameFromListServer

class TestServer(unittest.TestCase):

    def setUp(self):
        pass

    def testGet(self):
        test_text = '{"names":["Thomas, John P.","Gregory, Lucas A.","Samuels, Karl","Coen, Peter","Cohen, Greg","Douglass, Cathy R.","Gifford, Charles C.","Bassar, Ahmed H.","Hanson-Gretel, Andrew M."]}\r\n'
        for i in range(0,20):
            response = RandomNameFromListServer.test_handler(test_text)        
            self.assertRegexpMatches(response,"^\"[A-Za-z\-]+, [A-Za-z\-]+( \w\.){0,1}\"$")

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

'''
Created on 22 Jul 2013

@author: simone
'''
import unittest
from ipnotify.configuration import Configuration


class TestConfiguration(unittest.TestCase):

    def test_configuration(self):
#         self.assertEqual("first", "second", "failed")
        conf = Configuration()
        self.assertEquals(conf.get_param("email", "recipients"),
                         "simone@localhost", "fetching recipients failed")
        self.assertEquals(conf.get_param("ipsite", "url"),
                         "http://ip.42.pl/ip", "fetching ip checker url failed")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
# -*- coding: utf-8 -*-

# Copyright (C) 2013 Simone Soldateschi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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


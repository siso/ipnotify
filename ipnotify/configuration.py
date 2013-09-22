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

import logging
import os

import ConfigParser
from globals import *  # @UnusedWildImport

class Configuration:
    """read and and parse config file"""
    
    def __init__(self):
        '''determine config file path, load and parse it'''
        config_file_locations=[os.path.expanduser(CONFIG_FILE)]
        self.__config_file = None
        for f in config_file_locations:
            if os.path.exists(f):
                self.__config_file = f
                logging.debug("found config file: %s" % f)
                break
        if self.__config_file == None:
            logging.error(('configuration file missing. Default locations: %s' %
                           ", ".join(["%s" % f for f in config_file_locations])))
            raise Exception
        self.parse()

    def parse(self):
        """parse config file"""
        self.config = ConfigParser.ConfigParser()
        self.config.read(self.__config_file)

    def get_param(self, section, param, raw=1):
        """
        fetch a parameter from configuration file"""
        return self.config.get(section, param, raw)


class ConfigurationException(Exception):
    """
    class which implements exceptions of Configuration class
    """
    def __init__(self, errcode, errmsg):
        self.errcode = errcode
        self.errmsg = errmsg

    def __str__(self):
        return repr('(%d) %s' % (self.errcode, self.errmsg))


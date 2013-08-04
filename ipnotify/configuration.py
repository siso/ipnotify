import logging
import os

import ConfigParser


class Configuration:
    """read and and parse config file"""
    
    def __init__(self):
        '''determine config file path, load and parse it'''
        config_file_locations = ['/opt/ipnotify/etc/ipnotify.conf',
                                 './conf/ipnotify.conf',
                                 os.path.expanduser('~/.ipnotify/ipnotify.conf')
                                 ]
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

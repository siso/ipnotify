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

import os.path
from globals import *  # @UnusedWildImport
import logging
import sys


def create_default_conf():
    '''
    write default configuration file
    '''
    cfg = '''[smtp]
server: localhost
port: 25
#username: XXX
#password: XXX

[email]
# email subject
subject: ipnotify
# sender's email
sender: root@localhost
# recipipents separated by commas
recipients: root@localhost

[ipsite]
url: http://ip.42.pl/ip
'''
    with open(os.path.expanduser(CONFIG_FILE), 'w') as f:
        f.write(cfg)
        f.flush()

def create_default_log_conf():
    '''
    write default logging configuration file
    '''
    log_cfg = '''[loggers]
keys=root

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter, consoleFormatter

[logger_root]
level=INFO
handlers=fileHandler,consoleHandler

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=consoleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=handlers.RotatingFileHandler
level=DEBUG
args=(os.path.expanduser('~/.ipnotify/ipnotify.log'),'a','maxBytes=1024k','backupCount=5')
formatter=simpleFormatter

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s
datefmt=

[formatter_consoleFormatter]
format=(%(levelname)s) %(message)s
datefmt=
'''
    with open(os.path.expanduser(LOG_CONF_FILE), 'w') as f:
        f.write(log_cfg)
        f.flush()

def check_dir_home():
    '''
    check and create missing dirs and files
    '''
    if not os.path.isdir(os.path.expanduser(HOME_DIR)):
        check_dir(os.path.expanduser(HOME_DIR))
        create_default_conf()
        create_default_log_conf()
        return False
    return True

def check_dir(directory):
    '''
    Check dir, create it if necessary
    '''
    if not os.path.isdir(directory):
        logging.info("ipnotify directory '%s' is missing, creating it" % directory)
        try:
            os.mkdir(directory)
        except OSError as exc:
            logging.warn("error creating directory '%s'")
            raise exc
    
def check_env():
    '''
    check the environment, to ensure it can run smoothly
    '''
    import platform
    if platform.system() != 'Linux':
        print 'Unsupported OS. At the moment ipnotify can only run on GNU/Linux.'
        sys.exit(1)

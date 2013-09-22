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

import configuration
import libipnotify
from utility import *  # @UnusedWildImport

import logging.config

def start_logging():
    '''
    Start logging facility
    '''
    log_config_file_locations = [
                                 os.path.expanduser('~/.ipnotify/logging.conf'),
                                 ]
    log_config_file = None
    for f in log_config_file_locations:
        if os.path.exists(f):
            log_config_file = f
            logging.config.fileConfig(f)
            logging.debug("found log config file: %s" % f)
            break
    if log_config_file == None:
        logging.warn(('log configuration file missing. Default locations: %s' %
                      ", ".join(["%s" % f for f in log_config_file_locations])))
    
if __name__ == '__main__':
    # check environment before running
    check_env()
    
    # check '~/.ipnotify' and config files  exist
    if not check_dir_home():
        print ("This is the first time 'ipnotify' runs, please, configure "
               "'%s' according to your needs" % CONFIG_FILE)
        sys.exit(0)
    
    # start logging facility
    start_logging()
    
    logging.debug("ipnotify: starting...")
    
    # load config file
    conf = configuration.Configuration()
    
    # ########################################
    # DO STUFF
    
    lin = libipnotify.LibIpnotify()
    
    # access db
    lin.start_db()
    
    last_ip = lin.last_ip()[2]
    
    ipsite_url = conf.get_param("ipsite", "url", 0)
    current_ip = lin.get_ip(ipsite_url)
    if current_ip != last_ip:
        logging.info("ip address is changed (current: %s, previous: %s)" %
                     (current_ip, last_ip))
        logging.debug("store new ip in db")
        lin.store_ip(ipsite_url, current_ip)
        msg = "'%s' reports '%s'" % (ipsite_url, current_ip)
        logging.debug(msg)
        for recipient in conf.get_param("email", "recipients").split(','):
            logging.info('sending notification to \'%s\'' % recipient)
            lin.send_email(conf.get_param("smtp", "server"),
                           conf.get_param("smtp", "port"),
                           conf.get_param("email", "sender"),
                           recipient,
                           conf.get_param("email", "subject"),
                           msg)

    else:
        logging.info("ip address is unchanged")
    
    sys.exit(0)
    

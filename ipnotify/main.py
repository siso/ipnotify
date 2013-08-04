'''
Created on 22 Jul 2013

@author: simone
'''

import configuration
import libipnotify

import logging.config
import os.path
import sys

def start_logging():
    '''
    Start logging facility
    '''
    log_config_file_locations = [ '/opt/ipnotify/etc/logging.conf', 
                                 './conf/logging.conf',
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
    
if __name__ == '__main__':
    # start logging facility
    start_logging()
    
    logging.debug("ipnotify: starting...")
    
    # check '~/.ipnotify' exists
    check_dir(os.path.expanduser("~/.ipnotify"))
    
    # load config file
    conf = configuration.Configuration()
    
    # ########################################
    # DO STUFF
    
    lin = libipnotify.LibIpnotify()
    
    # access db
    lin.start_db(os.path.expanduser(conf.get_param("db", "file")))
    
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
    
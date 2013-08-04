'''
Created on 23 Jul 2013

@author: simone
'''

# from BeautifulSoup import BeautifulSoup  # @UnusedImport
from urllib import urlopen
import logging
import os.path
import sqlite3
import smtplib


class LibIpnotify(object):
    '''
    ipnotify main library
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def __del__(self):
        '''
        Destructor
        '''
        self.close_db()
    
    def send_email(self, server, port, sender, recipient, subject, msg):
        '''facility to send email message'''
        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        message = """From: %s
To: %s
Subject: %s

%s
""" % (sender, recipient, subject, msg)
        try:
            s = smtplib.SMTP(server, port)
            s.sendmail(sender, recipient, message)
            s.quit()
        except smtplib.SMTPException:
            logging.error('unable to send email')

    def get_ip(self, url):
        '''retrieve current public ip from online service'''
        logging.debug('parsing url: ' + url)
        fo = urlopen(url)
        html_doc = fo.read()
        fo.close()
#         soup = BeautifulSoup(html_doc)
        logging.info("get ip query - url:%s, ip:%s" % (url, html_doc))                                                        
        return html_doc

    def last_ip(self):
        '''
        Return last stored ip as tuple:
        
            (t, url, ip)
        
        t: time
        url: online service
        ip: ip address
        '''
        sql = "SELECT t, url, ip FROM ip ORDER BY t DESC LIMIT 1;"
        rs = self.query(sql)
        if len(rs) == 0:
            logging.debug("ip table is empty")
            return (None, None, None)
        for (t, url, ip) in rs:
            logging.debug("last ip query - t:%s, url:%s, ip:%s" % (t, url, ip))
        return (t, url, ip)
    
    def store_ip(self, url, ip):
        '''
        Store ip request in db
        '''
        sql = "INSERT INTO ip (url, ip) values ('%s', '%s')" % (url, ip)
        logging.debug("store ip - %s" % sql)
        self.query(sql)
        
    def start_db(self, dbfilename):
        '''access db, create a new db if it is missing'''
        if not os.path.isfile(dbfilename):
            logging.info("db file '%s' is missing, creating it" % dbfilename)
            self.__con = sqlite3.connect(dbfilename)  # @UndefinedVariable
            self.create_db_schema()
        else:
            logging.debug('database found (\'%s\')' % dbfilename)
            self.__con = sqlite3.connect(dbfilename)  # @UndefinedVariable
    
    def create_db_schema(self):
        '''create db schema'''
        cur = self.__con.cursor()
        sql = """CREATE TABLE ip (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        "t" timestamp default (strftime('%s', 'now')),
        "url" TEXT NOT NULL,
        "ip" TEXT NOT NULL);"""
        logging.debug(sql)
        cur.execute(sql)
        self.__con.commit()

    def close_db(self):
        self.__con.commit()
        self.__con.close()
    
    def query(self, sql):
        '''
        Execute query against db
        '''
        logging.debug('sql:%s' % sql)
        cur = self.__con.cursor()
        cur.execute(sql)
        self.__con.commit()
        return cur.fetchall()
    
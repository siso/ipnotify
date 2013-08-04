#!/usr/bin/python

'''
Created on 22 Jul 2013

@author: Simone Soldateschi

Examples: see README
'''

import runpy
import sys

sys.path.append('/opt/ipnotify')
# del sys.argv[0]  # Remove the runpy module from the arguments
runpy.run_module('ipnotify.main', run_name="__main__", alter_sys=True)

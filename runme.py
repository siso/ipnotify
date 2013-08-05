#!/usr/bin/python
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

@author: Simone Soldateschi

Examples: see README
'''

import runpy
import sys

sys.path.append('/opt/ipnotify')
# del sys.argv[0]  # Remove the runpy module from the arguments
runpy.run_module('ipnotify.main', run_name="__main__", alter_sys=True)


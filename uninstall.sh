#!/bin/bash
#
#   Package name:   ipnotify
#   Author:         Simone Soldateschi
#
#   Maintainer:     Simone Soldateschi
#
#   License:        GPL 2.0
#
#   Homepage:       https://github.com/siso/ipnotify/
#

#Name: ipnotify
#Requires: 

# Force the shell to exit immediately if something goes wrong
set -e

VERSION="0.1"

BINDIR="/usr/local/bin"
DESTDIR=/opt/ipnotify
CONFDIR=${DESTDIR}"/etc"
CRONDDIR="/etc/cron.d"
DATADIR=${DESTDIR}"/data"
LOGDIR=${DESTDIR}"/log"
MANPATH="/usr/local/share/man"
SCRIPTSDIR=${DESTDIR}"/ipnotify"

echo
echo "Uninstalling ipnotify from $DESTDIR"
echo

rm -rf $DESTDIR
rm $CRONDDIR/ipnotify

rm $MANPATH/man5/ipnotify.5.gz

rm $BINDIR/ipnotify

echo
echo "ipnotify uninstallation complete"

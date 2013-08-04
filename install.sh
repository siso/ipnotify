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
echo "Installing ipnotify to $DESTDIR"
echo

mkdir -p -m0755 $DESTDIR
mkdir -p -m0755 $CONFDIR
mkdir -p -m0755 $DATADIR
mkdir -p -m0755 $LOGDIR
mkdir -p -m0755 $MANPATH/man5
mkdir -p -m0755 $SCRIPTSDIR

install -m 0644 CHANGELOG $DESTDIR
install -m 0644 COPYING $DESTDIR
install -m 0644 README.md $DESTDIR

install -m 0644 conf/ipnotify.conf $CONFDIR
install -m 0644 conf/logging.conf $CONFDIR

install -m 0644 cron.d/ipnotify $CRONDDIR

install -m 0644 ipnotify/configuration.py $SCRIPTSDIR
install -m 0644 ipnotify/__init__.py $SCRIPTSDIR
install -m 0644 ipnotify/libipnotify.py $SCRIPTSDIR
install -m 0644 ipnotify/main.py $SCRIPTSDIR

install -m 0644 ipnotify.5.gz ${MANPATH}/man5

install -m 0755 ipnotify.sh $BINDIR/ipnotify

echo
echo "The cron execution of ipnotify is set to run every hour and at reboot by default."
echo "Edit /etc/cron.d/ipnotify to change cron execution."

echo
echo "ipnotify installation complete"

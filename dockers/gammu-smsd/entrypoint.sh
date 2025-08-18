#!/bin/sh

mkdir /var/spool/gammu/inbox/
mkdir /var/spool/gammu/outbox/
mkdir /var/spool/gammu/sent/
mkdir /var/spool/gammu/archive/
mkdir /var/spool/gammu/error/

# Start syslogd to forward logs to stdout
busybox syslogd -n -O /dev/stdout &

# Start Gammu SMSD
gammu-smsd -c /etc/smsd/smsdrc

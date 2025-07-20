#!/bin/sh

# Start syslogd to forward logs to stdout
busybox syslogd -n -O /dev/stdout &

# Start Gammu SMSD
gammu-smsd -c /etc/smsd/smsdrc

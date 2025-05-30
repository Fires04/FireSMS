FROM debian:stable-slim

RUN mkdir -p /var/spool/gammu/inbox/ /var/spool/gammu/outbox/ /var/spool/gammu/sent/ /var/spool/gammu/error/

RUN apt-get update && \
    apt-get install -y gammu gammu-smsd usbutils minicom

WORKDIR /etc/smsd

CMD ["gammu-smsd", "-c", "/etc/smsd/smsdrc"]

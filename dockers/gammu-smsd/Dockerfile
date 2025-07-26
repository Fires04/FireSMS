FROM debian:stable-slim

# Install required packages
RUN apt-get update && \
    apt-get install -y gammu gammu-smsd usbutils minicom busybox && \
    rm -rf /var/lib/apt/lists/*

# Set working directory for config
#WORKDIR /etc/smsd

# Copy config files
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]


HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
  CMD find /var/spool/gammu/outbox -type f -mmin +2 | grep -q . && exit 1 || exit 0

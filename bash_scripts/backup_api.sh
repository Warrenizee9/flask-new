#!/bin/bash

date=$(date +%Y-%m-%d-%H%M)
mkdir -p /home/ubuntu/backups
tar -czvf /home/ubuntu/backups/api_backup_$date.tar.gz /var/www/flask-new
find /home/ubuntu/backups/ -type f -mtime +7 -exec rm {} \;


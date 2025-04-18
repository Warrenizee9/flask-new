#!/bin/bash

echo "--- Updating System on $(date) ---" >> /var/log/update.log
sudo apt update -y >> /var/log/update.log
cd /var/www/flask-new
git pull >> /var/log/update.log
sudo systemctl restart flaskapi

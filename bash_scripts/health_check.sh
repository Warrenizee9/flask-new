#!/bin/bash

echo "$(date)" >> /var/log/server_health.log
echo "CPU Load:" >> /var/log/server_health.log
uptime >> /var/log/server_health.log
echo "Memory Usage:" >> /var/log/server_health.log
free -m >> /var/log/server_health.log
echo "Disk Usage:" >> /var/log/server_health.log
df -h >> /var/log/server_health.log
curl -s http://localhost:5000/ >> /var/log/server_health.log
echo "---------------------------" >> /var/log/server_health.log

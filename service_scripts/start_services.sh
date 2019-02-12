#!/bin/bash

echo "Starting all Personal Website services"

cp /var/www/Personal-Website/service_scripts/PersonalWebsiteGunicorn.service /etc/systemd/system/
cp /var/www/Personal-Website/service_scripts/PersonalWebsite /etc/nginx/sites-available/
cp /var/www/Personal-Website/service_scripts/PersonalWebsite /etc/nginx/sites-enabled/

systemctl daemon-reload

systemctl enable PersonalWebsiteGunicorn.service
systemctl restart PersonalWebsiteGunicorn.service

systemctl restart nginx

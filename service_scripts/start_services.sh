#!/bin/bash

echo "Starting all Personal Website services"

cp /var/www/Personal-Website/service_scripts/PersonalWebsiteGunicorn.service /etc/systemd/system/
cp /var/www/Personal-Website/service_scripts/PersonalWebsite /etc/nginx/sites-available/
cp /var/www/Personal-Website/service_scripts/PersonalWebsite /etc/nginx/sites-enabled/
cp /var/www/Personal-Website/poem_per_day/service_scripts/GeneratePoemPerDayGenerate.service /etc/systemd/system/
cp /var/www/Personal-Website/painting_per_day/service_scripts/GeneratePaintingPerDayGenerate.service /etc/systemd/system/

systemctl daemon-reload

systemctl enable PersonalWebsiteGunicorn.service
systemctl restart PersonalWebsiteGunicorn.service

systemctl enable GeneratePoemPerDayGenerate.service
systemctl restart GeneratePoemPerDayGenerate.service

systemctl enable GeneratePaintingPerDayGenerate.service
systemctl restart GeneratePaintingPerDayGenerate.service

systemctl restart nginx

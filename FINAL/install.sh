#!/bin/sh

echo "NGINX installing..."
sudo apt-get -y install nginx
echo "NGINX configuring..."
sudo cp configs/default /etc/nginx/sites-available/

echo "APACHE installing..."
sudo apt-get -y install apache2
echo "APACHE configuring..."
sudo cp configs/ports.conf /etc/apache2/
sudo cp configs/000-default.conf /etc/apache2/sites-available/
ln -s /etc/apache2/mods-available/cgi* /etc/apache2/mods-enabled
sudo mkdir -p /var/www/cgi-bin
sudo cp configs/sysinfo.cgi /var/www/cgi-bin/
chmod +x /var/www/cgi-bin/sysinfo.cgi

echo "sysstat package installing..."
sudo apt -y install sysstat

echo "Running..."
sudo /etc/init.d/nginx reload
sudo apachectl restart

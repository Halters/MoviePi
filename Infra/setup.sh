#!/bin/sh
echo "============================================================"
echo "|     Installing Apache2, MariaDB and Python3 with PIP     |"
echo "============================================================"
read -r -p "Install Apache2, MariaDB and Python3 with PIP ? [y/N] " response
response=${response,,}
if [[ "$response" =~ ^(yes|y)$ ]]; then
    sudo apt install apache2 mariadb-server mariadb-client python3 python3-pip libapache2-mod-wsgi-py3 python3-venv
    echo "============================================================"
    echo "|      Restarting MariaDB service and starting config      |"
    echo "============================================================"
    sudo systemctl restart mariadb.service
    sudo systemctl enable mariadb.service
    sudo mysql_secure_installation
    echo "============================================================"
    echo "|                  Installing PHP7.2-FPM                   |"
    echo "============================================================"
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:ondrej/php
    sudo apt update
    sudo apt install php7.2-fpm php7.2-common php7.2-mbstring php7.2-xmlrpc php7.2-soap php7.2-gd php7.2-xml php7.2-intl php7.2-mysql php7.2-cli php7.2-zip php7.2-curl php7.3-mbstring php7.2-mysqli php7.3-mysqli
fi
echo "============================================================"
echo "|                Adding MoviePi to Database                |"
echo "============================================================"
read -r -p "Import moviepi database scheme to MySQL and create user moviepi_api with passsword moviepi_api ? [y/N] " response
response=${response,,}
if [[ "$response" =~ ^(yes|y)$ ]]; then
    mysql -u root -p -h localhost < ../DB/moviepi_api.sql
fi
echo "============================================================"
echo "|             Disabling Apache default website             |"
echo "============================================================"
read -r -p "Disable Apache2 default website ? [y/N] " response
response=${response,,}
if [[ "$response" =~ ^(yes|y)$ ]]; then
    sudo a2dissite 000-default
    sudo systemctl restart apache2.service
    sudo systemctl enable apache2.service
fi
echo "============================================================"
echo "|                   Enabling API website                   |"
echo "============================================================"
sudo a2enmod wsgi
sudo cp ./flaskapi.com.conf /etc/apache2/sites-available/flaskapi.com.conf
sudo a2ensite flaskapi.com.conf
sudo mkdir -p /var/www/FLASKAPPS/moviepiapi/
cp ../API/moviepiapi/* /var/www/FLASKAPPS/moviepiapi/
python3 -m venv /var/www/FLASKAPPS/moviepiapi/
source /var/www/FLASKAPPS/moviepiapi/bin/activate
pip3 install wheel
pip install -r /var/www/FLASKAPPS/moviepiapi/requirements.txt
deactivate
cp ./moviepi.wsgi /var/www/FLASKAPPS/
sudo mkdir -p /var/www/moviepiapi.com/logs/
sudo chown -R www-data:www-data /var/www
echo "============================================================"
echo "|         Restarting PHP7.2-FPM, Apache2 services          |"
echo "============================================================"
sudo systemctl restart php7.2-fpm.service
sudo systemctl enable php7.2-fpm.service
sudo systemctl restart apache2.service
sudo systemctl enable apache2.service
echo "============================================================"
echo "|                  Installing PHPMyAdmin                   |"
echo "============================================================"
read -r -p "Install PHPMyAdmin ? [y/N] " response
response=${response,,}
if [[ "$response" =~ ^(yes|y)$ ]]; then
    sudo apt install phpmyadmin
    sudo apt autoremove
fi
echo "============================================================"
echo "|                  Setup script finished                   |"
echo "============================================================"
echo "============================================================"
echo "|          Running AutoUpdate Script for Database          |"
echo "============================================================"
echo "This script must be run contiuously, it is situated in :"
echo "      MoviePi/DB/suckings_script.py"
echo "You can use the package 'screen' to do so :"
echo "      apt install screen"
echo "      cd ../DB"
echo "      screen -d -m \"python3 suckings_script.py\""
echo "============================================================"
echo "|     Installing Apache2, MariaDB and Python3 with PIP     |"
echo "============================================================"
sudo apt install apache2 mariadb-server mariadb-client python3 python3-pip
echo "============================================================"
echo "       Restarting MariaDB service and starting config       "
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
echo "============================================================"
echo "|             Disabling Apache default website             |"
echo "============================================================"
sudo a2dissite 000-default
echo "============================================================"
echo "|                   Enabling API website                   |"
echo "============================================================"
sudo a2enmod wsgi
sudo cp ./flaskapi.com.conf /etc/apache2/sites-available/flaskapi.com.conf
sudo a2ensite flaskapi.com.conf
sudo mkdir -p /var/www/FLASKAPPS/moviepiapi/
cp -r ../API/* /var/www/FLASKAPPS/moviepiapi/
sudo mkdir -p /var/www/moviepiapi.com/logs/
sudp chown -R www-data:www-data /var/www
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
sudo apt install phpmyadmin
echo "============================================================"
echo "|          Installing Python depedencies for API           |"
echo "============================================================"
sudo pip3 install flask
sudo pip3 install flask_restful
sudo pip3 install flask_cors
sudo pip3 install sqlalchemy
sudo pip3 install pymysql
sudo pip3 install pyjwt
echo "============================================================"
echo "|                  Setup script finished                   |"
echo "============================================================"

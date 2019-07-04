#!/bin/sh
echo "============================================================"
echo "|            Pulling new version of repository             |"
echo "============================================================"
cd ..
git pull
cd -
echo "============================================================"
echo "|     Updating files of /var/www/FLASKAPPS/moviepiapi      |"
echo "============================================================"
cp ../API/moviepiapi/* /var/www/FLASKAPPS/moviepiapi/
source /var/www/FLASKAPPS/moviepiapi/bin/activate
pip install -r /var/www/FLASKAPPS/moviepiapi/requirements.txt
deactivate
sudo chown -R www-data:www-data /var/www/FLASKAPPS

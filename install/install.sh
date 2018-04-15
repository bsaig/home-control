#!/bin/sh

#This shell will install all the libraries and packages (including LAMP) to make our webserver & database work
#
#

echo ""
echo "Installation is going to start - Please follow Instruction"
echo ""


# 1 - "SYSTEM UPDATE & UPGRADE" (OK)
#------------------------------------------------
sudo apt-get -y update
sudo apt-get -y upgrade
#------------------------------------------------

# 2 - "MODIFICATION OF TEMP PRIVILEDGE" (OK)
#------------------------------------------------
sudo chown root:root /tmp
sudo chmod 1777 /tmp
#------------------------------------------------

# 3 - "INSTALLATION OF MYSQL SERVER" (OK)
#------------------------------------------------
#-------Will ask for the root password-----------
sudo apt-get -y install mysql-server-5.5
#------------------------------------------------

# 4 - "INSTALLATION OF TOOLS" (OK)
#------------------------------------------------
sudo apt-get -y install minicom
#tar in /home/pi
tar -xzf /home/pi/install/libraries/pyserial-3.0.1.tar.gz
cd pyserial-3.0.1/
sudo python setup.py install
cd
sudo rm -R pyserial-3.05/

tar -xzf /home/pi/install/libraries/MinimalModbus-0.7.tar.gz
cd MinimalModbus-0.7/
sudo python setup.py install
cd
sudo rm -R MinimalModbus-0.7/

tar -xzf /home/pi/install/libraries/RPi.GPIO-0.6.1.tar.gz
cd RPi.GPIO-0.6.1/
sudo python setup.py install
cd
sudo rm -r RPi.GPIO-0.6.1/

#------------------------------------------------


# 5 - "INSTALLATION OF NGNIX" (OK)
#------------------------------------------------
sudo apt-get -y install nginx
sudo service nginx start

echo ""
echo "Nginx default page should be acccessible at  the server IP"
echo ""
read -p "Can you see it ? (y/n) " REPLY
if [ "$REPLY" == "n" ]; then
echo "Check that ngnix was installed correctly."
fi
#------------------------------------------------

# 6 - "INSTALLATION OF PHP-FPM" (OK)
#------------------------------------------------
sudo apt-get -y install php5-fpm
#------------------------------------------------

# 7 - "INSTALLATION AND CONFIGURATION OF PHPMYADMIN" (OK)
#------------------------------------------------
echo ""
echo "Installing PHPmyadmin, when configuration screen appears press TAB then enter if using NGNIX"
echo ""

sudo apt-get -y install phpmyadmin	# Appuyer sur TAB et entrer pour le choix de la configuration
#Passwd: randompassword

# If the phpmyadmin page is not working HTTP 404 follow the steps bellow:
## "First, remove the symlink you just created by running:"
# rm -rf /usr/share/nginx/www
## "That won't delete phpMyAdmin, it'll just delete the symlink. Now we'll create a new one using:"
# sudo ln -s /usr/share/phpmyadmin/ /var/www/html/phpmyadmin
## "Since you've set root to /var/www/html, that's your "home" directory or root path that your server block uses. What the above command does is create a symlink from where the phpMyAdmin files are to your root directory."
## "Once the new symlink is there, you should be able confirm that by running:"
# ls -al /var/www/html
## "That should produce something that looks like:"
# lrwxrwxrwx 1 root root   22 Apr  4 14:31 phpmyadmin -> /usr/share/phpmyadmin/
## "Which means the symlink is valid and should now work when you visit:"
# http://IP_ADDR/phpmyadmin
## "Where IP_ADDR is your IP address."

sudo service php5-fpm restart
#------------------------------------------------

# 8 - "Installation of mysql python"
#------------------------------------------------
sudo apt-get -y install python-mysqldb
#------------------------------------------------

echo ""
echo "INSTALLATION DONE"
echo ""

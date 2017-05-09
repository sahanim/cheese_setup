# cheese_setup

mkdir vm_setup
cd vm_setup
sudo apt-get install git
git clone "https://github.com/sahanim/cheese_setup.git"

# dropbox setup
cd cheese_setup/dropbox
git clone "https://github.com/andreafabrizi/Dropbox-Uploader.git"
cd Dropbox-Uploader
sudo chmod +x dropbox_uploader.sh
sudo ./dropbox_uploader.sh
# Token = rpuajxG6Cq4AAAAAAAALvIc58HmL1E3_TN1zC8ptvFG0KseyDez5qrRgwADCnBmj
# dropbox API name is cheese_dropbox

#python
sudo apt-get install python-pip
sudo pip install ystockquote

#anaconda #numpy+mkl #scipy
cd ~/vm_setup/cheese_setup/anaconda
wget "http://repo.continuum.io/archive/Anaconda3-4.0.0-Linux-x86_64.sh"
sudo bash Anaconda*.sh

#documents
cd ~/vm_setup/cheese_setup/documents

#change timezone
cd /etc
sudo rm localtime
sudo ln -s /usr/share/zoneinfo/US/Eastern localtime

# cheese_setup

mkdir vm_setup
cd vm_setup
sudo apt-get install git
git clone "https://github.com/sahanim/cheese_setup.git"

# dropbox setup
cd dropbox
git clone "https://github.com/andreafabrizi/Dropbox-Uploader.git"
cd Dropbox-Uploader
sudo chmod +x dropbox_uploader.sh
./dropbox_uploader.sh
# dropbox API name is cheese_dropbox

#python

#anaconda #numpy+mkl #scipy

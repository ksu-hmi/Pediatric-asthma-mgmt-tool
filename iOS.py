brew install autoconf automake libtool pkg-config
brew link libtool
sudo easy_install pip 
sudo pip install Cython==0.29.10

#compile distribution
git clone git://github.com/kivy/kivy-ios
cd kivy-ios
./toochain.py build python3 kivy

#After previous codes run successfully, use tool chain script to create xcode project
./toolchain.py create <title> <app_directory>

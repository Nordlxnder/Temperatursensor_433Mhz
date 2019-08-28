sudo pacman -S cmake community/rtl-sdr
git clone https://github.com/merbanan/rtl_433.git
cd rtl_433/
mkdir build
cd build/
# Compile starten
cmake ../
# Make
make
# Install
sudo make install
# Test
rtl_433 -h

sudo apt update -y

sudo apt-get install build-essential libgl1-mesa-dev libglu1-mesa-dev libsdl2-dev libsdl2-image-dev libsdl2-ttf-dev libsdl2-gfx-dev libboost-all-dev libdirectfb-dev libst-dev mesa-utils xvfb x11vnc libboost-thread-dev libboost-python1.71-dev libboost-python1.71.0 libsdl2-gfx-dev libsdl2-ttf-dev libsdl2-image-dev libsdl2-dev libgl1-mesa-dev libboost-filesystem-dev -y

pip install --upgrade pip setuptools psutil wheel cmake

pip install gfootball

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install ./google-chrome-stable_current_amd64.deb -y

rm -f ./google-chrome-stable_current_amd64.deb

pip install -r ./scripts/install/requirements.txt

pip uninstall opencv-contrib-python opencv-python -y
pip install opencv-python==4.7.0.72
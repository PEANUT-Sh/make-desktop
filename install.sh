#!/bin/bash
USERNAME=$(whoami)
cd
echo "リポジトリのアップデート"
updt="sudo apt update"
eval $updt
echo "必要なもののインストール"
insta="sudo apt install python3 yad -y"
eval $insta
git clone https://github.com/PEANUT-Sh/make-desktop.git
cd /home/${USERNAME}/make-desktop
chmod +x ./make.sh
chmod +x ./main.py
chmod +x ./main.sh
echo "
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Name=デスクトップファイル生成くん
Path=/home/${USERNAME}/make-desktop/
Exec=python /home/${USERNAME}/make-desktop/main.py
StartupNotify=true
Terminal=false
"> /home/${USERNAME}/Desktop/main.desktop
chmod +x /home/${USERNAME}/Desktop/main.desktop
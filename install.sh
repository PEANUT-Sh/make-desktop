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
echo "[Desktop Entry]
Name=デスクトップファイル作成
Exec=/home/${USERNAME}/make-desktop/main.sh
Type=Application
" > /home/${USERNAME}/Desktop/main.desktop
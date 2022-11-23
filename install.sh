#!/bin/bash
cd
echo "リポジトリのアップデート"
updt="sudo apt update"
eval $updt
echo "必要なもののインストール"
insta="sudo apt install python3 yad -y"
eval $insta
git clone https://github.com/PEANUT-Sh/make-desktop.git
cd ./make-desktop
chmod +x ./make.sh
chmod +x ./main.py
chmod +x ./main.sh
echo "[Desktop Entry]
Name=デスクトップファイル作成
Exec=~/make-desktop/main.sh
Type=Application
" > ~/Desktop/make-desktop.desktop
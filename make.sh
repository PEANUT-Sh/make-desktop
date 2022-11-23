#!/bin/bash

echo ""
echo "make.sh"

#第一引数は名前
#第二引数はコマンド
#第三引数は保存場所とする

echo '$1 =' "$1"
echo '$2 =' "$2"
echo '$3 =' "$3"

wd="$3"
name="$1"
cmd="$2"

echo "$wd"

cd "$wd"

ss="`ls`"
echo "$ss"


echo "[Desktop Entry]
Name=${name}
Exec=${cmd}
Type=Application
" > ./${name}.desktop
#!/bin/bash

echo "######################################################"
echo "#                                                    #"
echo "#     #          #      #       #    #    ######     #"
echo "#    #   #   #  #     #  #     #   #     #           #"
echo "#   #     #    #    # #####   # ##      #####        #"
echo "#  #     #    #   #       #  #    #    #             # "
echo "# #           #  #       #  #       # ########       #"
echo "######################################################"
echo "make.sh"

#第一引数は名前
#第二引数はコマンド
#第三引数は保存場所とする

echo '$1 =' "$1"
echo '$2 =' "$2"
echo '$3 =' "$3"
echo '$4 =' "$4"

wd="$3"
name="$1"
cmd="$2"
icon="$4"

echo "$wd"

cd "$wd"

ss="`ls`"
echo "$ss"


echo "[Desktop Entry]
Name=${name}
Exec=${cmd}
Type=Application
Icon=${icon}
" > ./${name}.desktop
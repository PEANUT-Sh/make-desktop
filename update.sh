#!/bin/bash
(
    sleep 1
    wget https://github.com/PEANUT-Sh/make-desktop/raw/main/v.txt
    local=$(cat ./v.txt)
    github=$(cat ./v.txt.1)
    echo "${local}"
    echo "${github}"
    rm ./v.txt.1
) | yad --progress \
        --title="アップデートの確認"\
        --auto-close
echo "${local}"
echo "${github}"
if [ $local = $github ]; then
    yad --info --title="最新です"\
        --text="お使いのバージョンは最新です"\
        --center
else
    yad --info --title="最新ではありません"\
        --text="お使いのバージョンは最新ではありません\
        あなたのバージョン => ${local}\
        最新版 => ${github}"
fi
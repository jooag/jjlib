#! /usr/bin/env bash
if [[ -z "$(cat ~/.bashrc | grep "PYTHONPATH=\$PYTHONPATH:~/.pbin")" ]]; then
    printf "\nPYTHONPATH=\$PYTHONPATH:~/.pbin" >> ~/.bashrc
fi
mkdir -p ~/.pbin/jjlib
cp -r ./src ~/.pbin/jjlib
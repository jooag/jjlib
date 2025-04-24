#! /usr/bin/env bash
if [[ -z "$(cat ~/.bashrc | grep "PYTHONPATH=\$PYTHONPATH:~/.pbin")" ]]; then
    printf "\nPYTHONPATH=\$PYTHONPATH:~/.pbin" >> ~/.bashrc
fi
if [[ -z "$(cat ~/.zshrc | grep "PYTHONPATH=\$PYTHONPATH:~/.pbin")" ]]; then
    printf "\nPYTHONPATH=\$PYTHONPATH:~/.pbin" >> ~/.zshrc
fi
mkdir -p ~/.pbin/jjlib
cp -r ./src ~/.pbin/jjlib
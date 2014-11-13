#!/bin/bash

if [ ! -f "black.png" ]
then
    convert -size 320x240 xc:black black.png
fi

ffmpeg -loop 1 -i black.png -i "$1" -shortest -acodec copy "$2"

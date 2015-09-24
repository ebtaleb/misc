#!/usr/bin/env bash
for i in *.mp4
do
    new=`echo $i | cut -f1 -d'.'`
    new="$new"".aac"
    ffmpeg -i "$i" -vn -acodec copy "$new"
    new=""
done

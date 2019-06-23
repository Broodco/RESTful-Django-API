#!/bin/bash 
version_code=`aapt dump badging $* | grep versionCode | awk '{print $3}' | sed s/versionCode=//g | sed s/\'//g`
echo -n $version_code
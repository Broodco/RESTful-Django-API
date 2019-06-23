#!/bin/bash 
package_name=`aapt dump badging $* | grep package | awk '{print $2}' | sed s/name=//g | sed s/\'//g`
version_code=`aapt dump badging $* | grep versionCode | awk '{print $3}' | sed s/versionCode=//g | sed s/\'//g`
echo
echo package_name : $package_name
echo version_code : $version_code
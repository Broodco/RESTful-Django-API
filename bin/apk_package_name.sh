#!/bin/bash 
package_name=`aapt dump badging $* | grep package | awk '{print $2}' | sed s/name=//g | sed s/\'//g`
echo -n $package_name
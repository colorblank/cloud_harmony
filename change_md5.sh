#!/usr/bin/env bash 
    
for file in `ls $1/*`
do
md5 $file
echo -e A >> $file
md5 $file
done


#!/usr/bin/zsh


cat $1 | while read line;
do
  a=$(echo $line | cut -d " " -f 2)
  b=$(echo $line | cut -d " " -f 4)
  c=$(echo $line | cut -d " " -f 11)
  echo $a", "$b", "$c"," 
done


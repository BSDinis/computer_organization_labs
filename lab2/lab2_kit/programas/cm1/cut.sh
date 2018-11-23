#!/usr/bin/zsh


cat $1 | while read line;
do
  a=$(echo $line | cut -d "=" -f 2)
  a=$(echo $a | cut -d " " -f 1)
  b=$(echo $line | cut -d "=" -f 3)
  b=$(echo $b | cut -d " " -f 1)
  c=$(echo $line | cut -d "=" -f 4)
  c=$(echo $c | cut -d " " -f 1)
  d=$(echo $line | cut -d "=" -f 5)
  d=$(echo $d | cut -d " " -f 1)
  echo $a", "$b", "$c", "$d
done


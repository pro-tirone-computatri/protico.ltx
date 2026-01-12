#!/bin/bash


MFILE=dsp.mit.dirty.txt

if [ "$1" != "" ]; then 
  MFILE="$1"; 
fi


cat ${MFILE} |\
  sed 's/  */ /g' |\
  tr -d '\r' |\
  tr '\n' '$' |\
  sed 's/\$\$/\n\n/g' |\
  tr -d '$' |\
  tr 'a' 'a' |\
  sed 's/  */ /g' \
  >> x.txt
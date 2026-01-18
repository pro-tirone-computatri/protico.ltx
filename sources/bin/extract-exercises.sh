#!/bin/bash

# This file is part of the Open Source project 'proTironeComputatri'
# (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)


SOURCEFILE=oraltrack.md
TARGETFILE=exercises.md

if [ "$1" != "" ]; then SOURCEFILE=$1; fi

if ! [ -f $SOURCEFILE ]; then i
  echo "missing source file <$SOURCEFILE>"; 
  exit 0;
fi

UEBUNG="false"

if [ -f $TARGETFILE ]; then rm $TARGETFILE; fi

# use IFS= for preserving the indenting white spaces
cat $SOURCEFILE | while IFS= read line; do

  TOKEN=`echo $line | grep "uebung::end"`;
  if [ "$TOKEN" != "" ]; then 
    echo "found exercise end"; 
    echo -e "---\n" >> $TARGETFILE;
    UEBUNG="false";  
  fi
  
  if [ "$UEBUNG" = "true" ]; then 
    echo "$line" >> $TARGETFILE; 
  fi
  
  TOKEN=`echo $line | grep "uebung::start"`;
  if [ "$TOKEN" != "" ]; then echo "found exercise start"; UEBUNG="true"; fi

done
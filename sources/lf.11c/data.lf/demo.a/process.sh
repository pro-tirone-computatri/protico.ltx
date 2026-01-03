#!/bin/bash

cat MIT.dirty.txt |\
  sed 's/  */ /g' |\
  tr -d '\r' |\
  tr '\n' '$' |\
  sed 's/\$\$/\n\n/g' |\
  tr -d '$' |\
  tr 'a' 'a' |\
  sed 's/  */ /g' \
  >> x.txt
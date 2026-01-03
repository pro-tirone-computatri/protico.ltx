#!/bin/bash
# This file is part of the Open Source project 'proTironeComputatri'
# (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)

BD="../../do.publish/"

# for each LERNFELD and each of its subjects create a download directory:
# any such subject directory will contain its topic specific files
#

if [ -f ${BD} ]; then rm ${BD}; fi

mkdir -p ${BD}

find lf* -maxdepth 1 -type d | grep crx | while read d; do echo "creating crx lesson dir: $d"; mkdir -p $BD/$d; done
find lf* -maxdepth 1 -type d | grep sbj | while read d; do echo "creating sbj lesson dir: $d"; mkdir -p $BD/$d; done
find lf* -maxdepth 2 -type d | grep tpc | while read d; do echo "creating tpc lesson dir: $d"; mkdir -p $BD/$d; done


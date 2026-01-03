#!/bin/bash


find . -name zp.tex | while read f; do echo $f; cat $f | grep \\title{; done

find . -name header* | while read f; do echo $f; head -n2 $f; done
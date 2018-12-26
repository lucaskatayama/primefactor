#!/bin/bash

script=primefactor.py

rm -rf *.out
for file in $(ls *.in);
do
	filename=$(basename $file .in)
	if [[ -f ${filename}.ans ]]; then
	    echo ${file}

	    utime="$( TIMEFORMAT='%U';time ( python3.6 ${script} < ${file} > ${filename}.out ) 2>&1 1>/dev/null )"
		cputime_limit=$(echo "${utime}<3" | bc -l)
		if [[ ${cputime_limit} -eq 0 ]]; then
		    echo "CPU Time > 3s"
		fi

		result=$(diff -q ${filename}.ans ${filename}.out)
		if [[ ! -z ${result} ]];then
		    diff -y --suppress-common-lines ${filename}.ans ${filename}.out
		fi

		rm ${filename}.out

		echo '-------------------------------'
	fi
done






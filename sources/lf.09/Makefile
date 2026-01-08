# This file is part of the Open Source project 'proTironeComputatri'
# (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

BLD=../../built/lf.09
CCL=curriculum-check-list

lessons: lesson-ccl
	find . -maxdepth 1 -type d -name "sbj-*" | while read d; \
		do echo $$d; \
		( cd $$d; \
		  make lessons; \
			make clean; \
		) \
	done


clean:
	find . -maxdepth 1 -type d -name "sbj-*" | while read d; \
		do echo $$d; \
		( cd $$d; \
		  make clean; \
		) \
	done
	if [ -f ${CCL}.pdf ]; then rm ${CCL}.pdf; fi

lesson-ccl: ccl 
	mkdir -p ${BLD}
	mv ${CCL}.pdf ${BLD}/
	cp ${CCL}.md ${BLD}/

	
ccl:
	( cd sbj-00.curriculum && make ../${CCL}.pdf)


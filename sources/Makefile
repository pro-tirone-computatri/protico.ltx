# This file is part of the Open Source project 'proTironeComputatri'
# (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)

# files which resursively shall be erased for clearing the dev tree

EF="img-meta-data.json"

lessons:
	@find . -name "lf.*" -type d | while read dir; do \
		(cd $${dir} && make lessons); \
	 done

clear:
	@for fn in ${EF}; do \
		find . -name $${fn} | while read ff; do \
			echo erasing $${ff}; rm $${ff}; \
		done; \
	done; 
	
clean:
	@find . -name "*bkp" | while read f; do rm $$f; echo "erasing $$f"; done
	@find . -type d -name "lf.*" | while read d; do echo $$d; ( cd $$d && make clean); done

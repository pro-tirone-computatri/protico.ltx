# This file is part of proScientia.ltx
# (c) 2022 Karsten Reincke (https://github.com/kreincke/proScientia.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)

#LATEX=latex
LATEX=pdflatex

AUX_EXTS=url bbl blg aux dvi toc log lof nlo nls ilg ils ent out log bcf xml nav snm vrb
RES_EXTS=ps pdf
RESULTS=results

LNX_TD="../.."
PTC_TD="../${LNX_TD}"
BD=${PTC_TD}/built

LVZ="fi-literaturverzeichnis"

help:
	echo "make [ lesson | lvz | YOURFILE.pdf | help]"


lessons: lvz
	mkdir -p ${BD}
	mv ${LVZ}.pdf ${BD}
	@ tree ${BD}	

lvz:
	@ make ${LVZ}.pdf

check:
	@ echo "### `date +'%Y%m%dT%H%M%S'`"
	@ echo "### checking library entries of ${LVZ}"
	@ $(LATEX)  ${LVZ}.tex
	@ biber ${LVZ}.bcf
	@ echo "nach ${BD}"

.SUFFIXES: .tex .dvi .ps .pdf .rtf

.tex.pdf:
	@ echo "### `date +'%Y%m%dT%H%M%S'`"
	@ echo "### converting $< to $@"
	@ $(LATEX) $<
	@ biber `basename $< .tex`
	@ makeindex `basename $< .tex`.nlo -s ../../cfg.gl/nomencl.ist -o `basename $< .tex`.nls
	@ $(LATEX) $<
	@ $(LATEX) $<

clear:
	$(foreach EXT, ${AUX_EXTS}, if [ ! "x`ls *.${EXT} 2>/dev/null`" = "x" ]; then rm *.${EXT}; fi;)

clean:	clear
	$(foreach EXT, ${RES_EXTS}, if [ ! "x`ls *.${EXT} 2>/dev/null`" = "x" ]; then rm *.${EXT}; fi;)



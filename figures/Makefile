TEX = unit_circle.tex \
	   segment.tex \
	   lerp.tex

PDFS = $(TEX:.tex=.pdf)
PNGS = $(TEX:%.tex=../images/%.png)

all: $(PNGS) ../images/fib.png

clean:
	$(RM) $(PDFS)
	$(RM) *.aux *.log *.dvi

%.pdf: %.tex
	pdflatex $<

../images/fib.png: fib.py
	python fib.py | dot -Tpng > $@

$(PNGS): ../images/%.png: %.pdf
	convert -density 300 -quality 90 -resize '50%' $< $@

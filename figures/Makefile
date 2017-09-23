SRCS = unit_circle.tex \
	   segment.tex \
	   lerp.tex

PDFS = $(SRCS:.tex=.pdf)
PNGS = $(SRCS:%.tex=../images/%.png)

all: $(PNGS)

clean:
	$(RM) $(PDFS)
	$(RM) *.aux *.log *.dvi

%.pdf: %.tex
	pdflatex $<

$(PNGS): ../images/%.png: %.pdf
	convert -density 300 -quality 90 -resize '50%' $< $@

SRCS = unit_circle.tex

PDFS = $(SRCS:.tex=.pdf)

PNGS = $(SRCS:.tex=.png)

all: $(PNGS)

clean:
	$(RM) $(PDFS) $(PNGS)
	$(RM) *.aux *.log *.dvi

%.pdf: %.tex
	pdflatex $<

%.png: %.pdf
	convert -density 300 -quality 90 -resize '50%' $< $@
	mv $@ ../images/
	$(MAKE) clean

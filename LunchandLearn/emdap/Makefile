# Makefile for Beamer crisis-room deck
# Usage:
#   make            # build PDF
#   make watch      # continuous build on changes
#   make render     # export slide PNGs + contact sheet (needs ImageMagick)
#   make clean      # remove aux files
#   make distclean  # remove aux files + PDF + render outputs

TEX      := emdap.tex
PDF      := $(TEX:.tex=.pdf)
OUTDIR   := .
RENDERDIR:= render

LATEXMK  := pdflatex
LATEXMKFLAGS := -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
                -synctex=1 -outdir=$(OUTDIR)

# IM       := magick
# DENSITY  := 200

.PHONY: all pdf watch clean distclean render contact_sheet

all: pdf

pdf: $(PDF)

$(PDF): $(TEX)
	$(LATEXMK) $(LATEXMKFLAGS) $<

watch:
	$(LATEXMK) $(LATEXMKFLAGS) -pvc $(TEX)

render: pdf
	mkdir -p $(RENDERDIR)
	# Export each slide to PNG (Beamer pages are 1-indexed)
	$(IM) -density $(DENSITY) $(PDF) -quality 95 $(RENDERDIR)/slide-%02d.png
	$(MAKE) contact_sheet

contact_sheet:
	# Build a quick contact sheet (5x5) for visual QC
	$(IM) montage $(RENDERDIR)/slide-*.png -tile 5x5 -geometry +6+6 $(RENDERDIR)/contact_sheet.png

clean:
	$(LATEXMK) -c -outdir=$(OUTDIR) $(TEX) || true
	# latexmk -c sometimes leaves these behind
	rm -f *.nav *.snm *.toc *.out *.vrb

distclean: clean
	rm -f $(PDF)
	rm -rf $(RENDERDIR)

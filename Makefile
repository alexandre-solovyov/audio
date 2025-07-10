
html = $(wildcard *.xhtml)
txt  = $(patsubst %.xhtml, %.txt, $(html))

all: $(txt)

%.txt: %.xhtml Makefile
	html2text $< | sed "s/<?xml version='1.0' encoding='utf-8'?>//" > $@

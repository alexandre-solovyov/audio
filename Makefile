
html = $(wildcard *.xhtml)
txt  = $(patsubst %.xhtml, out/%.txt, $(html))
wav  = $(patsubst %.xhtml, out/%.wav, $(html))
mp3  = $(patsubst %.xhtml, res/%.mp3, $(html))
temp = 1.25
rate = 96


all: $(txt) $(wav) $(mp3)


out/%.txt: %.xhtml
	html2text $< | sed "s/<?xml version='1.0' encoding='utf-8'?>//" > $@

out/%.wav: out/%.txt
	cat $< | ~/piper/piper --model ~/piper/ru_RU-irina-medium.onnx --output-file $@

res/%.mp3: out/%.wav
	ffmpeg -i $< -vn -ar 44100 -ac 2 -b:a $(rate)k -af atempo=$(temp) $@

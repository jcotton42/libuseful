all: sorts searches index master gui

%: %.md
	markdown $< > $@.html

clean:
	rm *.html

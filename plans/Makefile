all: sorts searches index master gui re

%: %.md
	markdown $< > $@.html

clean:
	rm *.html

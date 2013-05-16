all: sorts searches index master

%: %.md
	markdown $< > $@.html

clean:
	rm *.html

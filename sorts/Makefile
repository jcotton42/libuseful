.PHONY: all clean

all: *.py

clean:
	rm -rf __pycache__

%.py:
	python -m py_compile $@

%.md:
	markdown $@ > $(@:.md=.html)

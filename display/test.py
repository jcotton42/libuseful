from progress import *
from time import sleep
from random import randint
def test():
	p = ProgressBar(100, twidth = 10)
	while True:
		for i in range(101):
			p.update(i)
			sleep(0.05)
		for i in range(100, 0, -1):
			p.update(i)
			sleep(0.05)
if __name__ == "__main__":
	test()

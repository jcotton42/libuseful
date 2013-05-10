from progress import ProgressBar
import time
p = ProgressBar(twidth = 100, blankchar="=", fillchar="+")
for i in range(101):
	p.update(i)
	time.sleep(0.1)
print

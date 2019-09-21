from duplicate import *
import re

def fetcher():
	with open("test.txt", "r", encoding="utf-8") as fobj:
		text = fobj.read()

	matches = re.findall(r'https://post-phinf\.pstatic\.net[^"&? ]+', text)

	out_str = "\n".join(matches)

	with open("output.txt", "w") as outp:
		outp.write(out_str)
	print(matches)
	rem_duplicate()
fetcher()
import os
import sys
def rem_duplicate():
	lines_seen = set()  # holds lines already seen
	outfile = open('links.txt', "w")
	infile = open('output.txt', "r")
	print ("The file output.txt is as follows")
	for line in infile:
		print (line)
		if line not in lines_seen:  # not a duplicate
			outfile.write(line)
			lines_seen.add(line)
	outfile.close()
	print ("The file links.txt is as follows")
	for line in open('links.txt', "r"):
		print (line)

	os.rename('links.txt','url_here.txt')
	os.remove("output.txt")
	os.remove("test.txt")

import os
from glob import glob

def linesInFile(filename:str, includeBlank:bool=True):

	try:
		file = open(filename,"r")
		contents = file.read()
	except:
		try:
			file = open(filename, encoding="utf8")
			contents = file.read()
		except:
			print(f"Failed to read file '{filename}'")
			return 0

	# Reading from file

	collist = contents.split("\n")

	count = 0
	count_all = 0
	for i in collist:

		count_all += 1

		if i:
			count += 1

	if includeBlank:
		return count_all
	else:
		return count

def recursiveFilesInDir(path:str, pattern:str="*.*"):
	return [y for x in os.walk(path) for y in glob(os.path.join(x[0], pattern))]

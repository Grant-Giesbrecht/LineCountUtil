import sys
from linecountutil import *

print("test")

print(sys.argv[1:])

# Get path
if len(sys.argv) > 1:
	path = sys.argv[1]
else:
	path = "."

if len(sys.argv) > 2:
	pattern = sys.argv[2]
else:
	pattern = "*.*"

# Get keep blanks?
if len(sys.argv) > 3:
	keepBlanks = sys.argv[3].upper() == "TRUE"
else:
	keepBlanks = True

if len(sys.argv) > 4:
	showDetails = sys.argv[4].upper() == "TRUE"
else:
	showDetails = True


files = recursiveFilesInDir(path, pattern)

count = 0
idx = 1
for f in files:
	fv = linesInFile(f, keepBlanks)
	count += fv

	if showDetails:
		print(f"[{idx}]")
		print(f"    File: {f}")
		print(f"    No. Lines: {fv}")

	idx += 1

print(f"\n*****************************************")
if count < 1e3:
	print(f"Total Number of Lines: {count}")
else:
	print(f"Total Number of Lines: {count/1e3}K")
print(f"Number of files: {len(files)}")
print(f"Avg. Lines per File: {count/len(files)}")

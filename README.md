# LineCountUtil
Count the lines of code in your folder!

## How to Use It

Call the Python script 'lcount.py' and give it optional parameters for how to count:

*Argument 1:* Path to directory in which to count the lines of all files in that directory and its subfolders (default: ".")

*Argument 2:* Regex to filter specific files, such as of one extension (default: "*.*")

*Argument 3:* (True/False) Count blank lines? (default: True)

*Argument 4:* (True/False) Show detailed output? (default: True)

### Example: 
`python lcount.py "./path/to/place/to/count/" "*.py" True False`

"""
Read a text file 'report.txt' line by line and display each word separated by a #.
"""
file = open("Assets\\report.txt", 'r')
text = file.readlines()
for lines in text:
    lines = lines.replace(" ", "#")
    print(lines)
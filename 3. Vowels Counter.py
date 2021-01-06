"""
Write program using function to read a  text file report.txt,
line by line and print it and to count the number of vowels present in it.
"""


def vowelcounter(line):
    vowl = 0
    vol = ['a', 'e', 'i', 'o', 'u']

    for i in line.lower():
        if i in vol:
            vowl += 1
    return vowl


totalVowls = 0
file = open("Assets\\report.txt", 'r')
text = file.readlines()

for lines in text:
    vols = vowelcounter(lines)
    print(lines, "Vowels in this line: ", vols)
    totalVowls += vols

print("Total Vowels in this File: ", totalVowls)

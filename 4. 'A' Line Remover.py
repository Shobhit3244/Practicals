"""
Write Python program to remove all the lines that
contain the character `a' in "story.txt" file and
write it to another file "newStory.txt"
"""
open("Assets\\newStory.txt", mode="w")
file = open("Assets\\story.txt", 'r')
text = file.readlines()
file.close()
for lines in text:
    if 'a' in lines.lower():
        continue
    print(lines)
    with open("Assets\\newStory.txt", mode="a") as newStory:
        newStory.write(lines)

"""
Create a binary file 'marks.bin' with roll number, name
and marks. Input a roll number and update the marks.
"""


def file_editor(roll, name, marks):
    wfile = open('Assets\\marks.bin', 'a')
    text = str(roll) + ":" + name + ":" + str(marks) + '\n'
    wfile.write(text)
    wfile.close()


def file_checker(roll):
    rfile = open('Assets\\marks.bin', 'r')
    fcont = rfile.readlines()
    rfile.close()
    for itm in fcont:
        itm = itm.replace("\n", "")
        itm_lst = itm.split(':')
        if roll == int(itm_lst[0]):
            print("Name: {} \nMarks: {}".format(itm_lst[1], itm_lst[2]))
            return
    else:
        print("Roll Number Not Found!"+'\n'+"File Contents: ")
        print(fcont)
        return


g = str(input("Would you like to add Students to Student list [y/n]: "))
if g.lower() == 'y':
    while True:
        h = int(input("Enter Roll number: "))
        i = str(input("Enter Students Name: "))
        j = int(input("Enter Student's Marks: "))
        file_editor(h, i, j)
        x = str(input("Would you like to Add more Student Data [y/n]: "))
        if x.lower() == 'n':
            break
    print("Student Data Added Successfully!")
    input("Press Enter to Proceed Further...")

while True:
    x = str(input("Would you like to check Student list [y/n]: "))
    if x.lower() == 'n':
        break
    y = int(input("Enter Student Roll No.: "))
    file_checker(y)
print("Thanks")

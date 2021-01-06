"""
Create a binary file 'student.dat' with name and roll number.
Search for a given roll number and display the name,
if not found display appropriate message.
"""
import pickle
StdData = {"Roll": "StdNm"}


def file_creator():
    while True:
        roll = int(input("Enter Student's Roll No.: "))
        std_nm = str(input("Enter Student's Name: "))
        StdData[roll] = std_nm
        z = str(input("Would you like to add more Students to Student list [y/n]: "))
        if z.lower() == 'n':
            break
    file = open('Assets\\student.dat', 'rb')
    dtc = pickle.load(file)
    file.close()
    dtc.update(StdData)
    print(dtc)
    file = open('Assets\\\student.dat', 'wb')
    pickle.dump(dtc, file)
    file.close()


def file_reader(roll):
    file = open('Assets\\student.dat', 'rb')
    cont = pickle.load(file)
    file.close()
    if roll in cont:
        return cont.get(roll)
    print("{} \n The Roll Number You Entered is not assigned to any Student Would you like to ".format(cont))
    d = str(input("add it to the database? [y/n]: "))
    if d.lower() == 'y':
        file_creator()
        return "Data Added Successfully!"
    else:
        return "Ok!"


g = str(input("Would you like to add Students to Student list [y/n]: "))
if g.lower() == 'y':
    file_creator()
    print("Data Created Successfully!")
    input("Press Enter to Proceed Further...")

while True:
    x = str(input("Would you like to check Student list [y/n]: "))
    if x.lower() == 'n':
        break
    y = int(input("Enter Student Roll No.: "))
    print(file_reader(y))

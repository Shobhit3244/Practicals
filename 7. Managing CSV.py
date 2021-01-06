"""
Create a csv file 'contacts.csv' with four fields
( name, e-mailID, contact_no, DOB). Enter 5 records,
read the file and display the records.
"""
import csv


def add_contacts():
    with open('Assets\\contacts.csv', mode='a') as contacts:
        cont_edtr = csv.writer(contacts, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        name = str(input("Enter Contact Name: "))
        mail = str(input("Enter E-mail ID: "))
        numb = int(input("Enter Phone Number: "))
        dob = str(input("Enter Date of Birth: "))
        clist = [name, mail, numb, dob]
        cont_edtr.writerow(clist)


g = str(input("Would you like to add Someone to Contacts? [y/n]: "))
if g.lower() == 'y':
    while True:
        add_contacts()
        x = str(input("Would you like to Add more Contacts? [y/n]: "))
        if x.lower() == 'n':
            break
    print("Contacts Added Successfully!")
    input("Press Enter to Proceed Further...")


with open('Assets\\contacts.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row == []:
            continue
        print(f"\nContact Name: {row[0]}\nEmail Id: {row[1]}\nPhone Number: {row[2]}\nDate of Birth: {row[3]}\n")
        line_count += 1
    print(f'Processed {line_count} lines. Including Page Header')
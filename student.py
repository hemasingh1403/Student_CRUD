import os

# Function to insert records into the file
def insert_records():
    f = open("iics.txt", "a")  # Open the file in append mode
    while(True):
        roll = input("enter the roll no.=")  # Get roll number
        name = input("enter the name=")  # Get name
        course = input("enter the course name=")  # Get course name
        dob = input("enter the date of birth=")  # Get date of birth
        phone = input("enter the phone no.=")  # Get phone number
        add = input("enter the address=")  # Get address
        # Write the collected data to the file
        f.write(roll + "\t" + name + "\t" + course + "\t" + dob + "\t" + phone + "\t" + add + "\n")
        ans = input("are you exit?y/n")  # Ask if the user wants to exit
        if ans == "y":
            break
    print("record insert successfully!!!!")
    f.close()  # Close the file

# Function to display all records
def display_records():
    f = open("iics.txt", "r")  # Open the file in read mode
    print("roll\tname\tcourse\tdob\tphone\t\tadd")  # Print the header
    for rec in f:  # Loop through each record in the file
        print(rec, end="")  # Print each record
    f.close()  # Close the file

# Function to search for a particular record
def search_records():
    f = open("iics.txt", "r")  # Open the file in read mode
    r = int(input("enter roll no."))  # Get the roll number to search
    for line in f:  # Loop through each record in the file
        rec = line.split("\t")  # Split the record into fields
        if int(rec[0]) == r:  # Check if the roll number matches
            print("roll\tname\tcourse\tdob\tphone\t\tadd")  # Print the header
            print(rec[:])  # Print the matching record
            break
    else:
        print("record not found")  # Print if no matching record is found
    f.close()  # Close the file

# Function to delete a record
def delete_records():
    f = open("iics.txt", "r")  # Open the original file in read mode
    g = open('temp.txt', "w")  # Open a temporary file in write mode
    r = int(input("enter roll no."))  # Get the roll number to delete
    fg = 0  # Flag to check if record is found
    for line in f:  # Loop through each record in the file
        rec = line.split("\t")  # Split the record into fields
        if int(rec[0]) == r:  # Check if the roll number matches
            fg = 1  # Set flag if record is found
        else:
            g.write(line)  # Write the record to the temporary file if not matched
    f.close()  # Close the original file
    g.close()  # Close the temporary file
    if fg == 0:
        print("not found records")  # Print if no matching record is found
    else:
        print("delete successfully!!!")  # Print if record is deleted
    os.remove("iics.txt")  # Remove the original file
    os.rename("temp.txt", "iics.txt")  # Rename the temporary file to original file name

# Function to update a record
def update_records():
    f = open("iics.txt", "r")  # Open the original file in read mode
    g = open("temp.txt", "w")  # Open a temporary file in write mode
    r = int(input("enter roll no. update:"))  # Get the roll number to update
    title = ['roll', 'name', 'course','DOB', 'phone', 'address']  # Titles for the fields
    fg = 0  # Flag to check if record is found
    for i in f:  # Loop through each record in the file
        rec = i.split("\t")  # Split the record into fields
        if rec[0] == str(r):  # Check if the roll number matches
            fg = 1  # Set flag if record is found
            while(True):
                # Display options to edit fields
                print("press", 1, "to edit", title[1])
                print("press", 2, "to edit", title[2])
                print("press", 3, "to edit", title[3])
                print("press", 4, "to edit", title[4])
                print("press", 5, "to edit", title[5])
                print("e for exit")
                ch = input("select the option")
                if ch == "1":
                    n = input("enter new name :")
                    rec[1] = n
                elif ch == "2":
                    n = input("enter new course :")
                    rec[2] = n
                elif ch == "3":
                    n = input("enter new DOB. :")
                    rec[3] = n
                elif ch == "4":
                    n = input("enter new phone no. :")
                    rec[4] = n
                elif ch == "5":
                    n = input("enter new address :")
                    rec[5] = n
                elif ch == "e" or ch == "E":
                    break
            g.write("\t".join(rec) + "\n")  # Write the updated record to the temporary file
        else:
            g.write(i)  # Write the unchanged record to the temporary file
    if fg == 0:
        print("record not found")  # Print if no matching record is found
    else:
        print("update successfully!!!!")  # Print if record is updated
    f.close()  # Close the original file
    g.close()  # Close the temporary file
    os.remove("iics.txt")  # Remove the original file
    os.rename("temp.txt", "iics.txt")  # Rename the temporary file to original file name

# Main menu to choose operation
print("1.Insert Records\n2.display all records\n3.search a particular records\n4.delete a records\n5.update a records")
ch = int(input("enter your choice:"))  # Get user choice
if ch == 1:
    insert_records()  # Call insert records function
elif ch == 2:
    display_records()  # Call display records function
elif ch == 3:
    search_records()  # Call search records function
elif ch == 4:
    delete_records()  # Call delete records function
elif ch == 5:
    update_records()  # Call update records function

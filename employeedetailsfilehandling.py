#Task 2: Read Employee Details
#Create a text file named employee.txt and write the following content into it:
#Employee ID: 105
#Name: Vaishak
#Department: Python Development
#Designation: Software Developer
#Salary: 35000

#Requirements:
#1. Open the employee.txt file in read mode ("r").
#2. Read the entire content of the file.
#3. Display the content using print().
#4. Close the file.
#5. Display whether the file is closed or not.

fileptr=open(r"C:\SMEC\filehandling\employee.txt","r")
content=fileptr.read()
print(content)
fileptr.close()
print("IS FILE CLOSED ? :", fileptr.closed)
#Task 1: Read File Content

#Create a text file named student.txt and write the following content into it:
#Name: Anoop
#Age: 27
#Course: SOC Analyst
#Institute: ABC Technologies

#Requirements:
#1. Open the student.txt file in read mode ("r").
#2. Read the entire content of the file.
#3. Display the content using print().
#4. Close the file.
#5. Display whether the file is closed or not.

fileptr=open(r"C:\SMEC\filehandling\student.txt","r")
content=fileptr.read()
print(content)
fileptr.close()
print("IS FILE CLOSED TRUE OR FALSE ?:",fileptr.closed)
"""
fileptr=open(r"C:\SMEC\filehandling\samplefile.txt","r")
if fileptr:
    print("FILE IS OPENED SUCCESSFULLY.......")
print(fileptr.closed)
fileptr.close()
print(fileptr.closed)

"""
"""
filenew=open(r"C:\SMEC\filehandling\samplefile.txt","r")
content=filenew.read()
print(content)
filenew.close()

""" 
with open(r"C:\SMEC\filehandling\samplefile.txt","r") as filenew:
    content=filenew.read()
    print(content)
    filenew.close()

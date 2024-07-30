import os

#Read the existiing file
def read(file_name):
    with open(file_name,"r") as file:
        return file.read()
#Calling the read function
file_name="outputs.txt"
value=read(file_name)



#Creating a new file 
Data = input("Enter the content:")

# define a new file name for creating

newfile_name = "newoutput.txt"

# Open the file in write mode and store the value

with open(newfile_name, "w") as file:
    file.write(Data)

#print the success message is it stored in a file
    
print("The file is created and the value is stored in:",newfile_name)



#Delete the previous file name(outputs.txt)
os.remove(file_name)
print(f"{file_name} has been deleted.")

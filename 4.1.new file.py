import os
#adding the file content to the old file to the new file
def add_file(file_name,newfile_name):
#Opening the old file file content in a read mode
    with open  (file_name,"r") as files:
        data=files.read()
#Adding the old file content to new file using the append mode
    with open(newfile_name,"a") as newfiles:
        newfiles.write(data)
#File names are

file_name="outputs.txt"
newfile_name="newoutput.txt"


#Calling the function

add_file(file_name,newfile_name)

#Delete the previous file name(outputs.txt)

os.remove(file_name)
print(f"{file_name} has been deleted.")

print("Content of",file_name," has been added to",newfile_name)

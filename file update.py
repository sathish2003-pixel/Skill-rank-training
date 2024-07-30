import os

# Define the variable to be stored
content = input("Enter the content")
# Define the file name have to store the variable
file_name = "output.txt"

# Open the file in write mode and store the variable
with open(file_name, "w") as file:
    file.write(content)

#print the success message is it stored in a file  
print(f"The variable has been stored in {file_name}.")

#Update the file with another variable function
def update_variable(file_name, new_data):
    with open(file_name, "a") as file:
        file.write(new_data)
new_data="Bye bye"
#Calling the update function
update_variable(file_name,new_data)

#read the variable
def read(file_name):
    with open(file_name,"r") as file:
        return file.read()
    #Calling the read function
value=read(file_name)


#Delete the file function
def delete(file_name):
    #the file is exists remove that 
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"{file_name} has been deleted.")
    else:
        print(f"{file_name} does not exist.")
#The value is returned the delete function is work(If the if condition is true)
if value:
    delete(file_name)

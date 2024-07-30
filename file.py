# Define the variable to be stored
content = input("Enter the content")
# Define the file name have to store the variable
file_name = "outputs.txt"

# Open the file in write mode and store the variable
with open(file_name, "w") as file:
    file.write(content)

#print the success message is it stored in a file  
print(f"The variable has been stored in {file_name}.")


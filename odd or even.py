# Program to find the number is odd or even 
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

#Input from the user
number=int(input("Enter an integer: "))

#Calling the function
result = check_even_odd(number)

# Print the result
print("The number",number,"is",result)

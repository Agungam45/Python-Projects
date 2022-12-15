
#Ask the user what kind of equation they would like to do
equation_type = input("What kind of math do you want to do? ")
#Convert the equation into lowercase 
equation_type = equation_type.lower()

#Enter the 1st and 2nd number 
first_number = float(input("What is the 1st number? "))
second_number = float(input("What is the 2nd number? "))

if equation_type == "add" or equation_type == "addition":
        result = first_number + second_number
elif equation_type == "subtract" or equation_type == "subtraction":
        result = (first_number - second_number)
elif equation_type == "multiply" or equation_type == "multiplication":
        result = first_number * second_number
elif equation_type == "divide" or equation_type == "division":
        result = first_number / second_number
else:
        print("not a valid entry :/")
        equation_type = lower(input("What kind of math do you want to do? "))
print(result)
again = input("Would you like to do another math problem? y/n")
if again == 'y':
        True 
else:
        print("Thanks for your time!")
                

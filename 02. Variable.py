# variables reserves space in memory to store data, which will be used in the program later.
# Unlike aother programming languages, we don't need to specify the datatype for the variables
# Python automatically assign datatype based on the value stored in the variable
# we can convert one varible type to another using typecasting e.g str(int_var) will convert int variable "int_var" into string variable
# the rule for the variable name is that it can only contain words, numbers and underscore.
# Format:       Name = Value

Name = "Hussain Abdullah"       #string Variable
Gender = 'M'                    #char Variable
Age = 20                        #int Variable
GPA = 3.71                      #float Variable
Bool = False                    #bool Variable

#....................................... Printing Values of variables ....................................................
# We can print value of any variable using print function

print(Name)
print(Gender)
print(Age)
print(GPA)
print(Bool)

#............................................... Cancatination ...........................................................
# To print different types of variables in single print statement, we have to cancatinate these variables. + in print is used for cancatination.
# We can cancatinate only strings, therefore we have to typecast every other variable into strings as well.

print("Name = "+Name+". Gender = "+Gender+". Age = "+str(Age)+". GPA = "+str(GPA)+".Bool = "+str(Bool)+".")

#........................................... Getting input from User ......................................................
# To get input from user, we can use input() function
# Format:       variable = input("prompt message")

var1 = input("Input some string: ")
print("You entered: "+var1)

# The input() stores input as string by default. If we want the data to be in other format, we can typecast the variable

num1 = int(input("Enter number to find its square: "))
num1 *= num1
print("Square of number you entered is: "+str(num1))

input("\nPress any key to exit")


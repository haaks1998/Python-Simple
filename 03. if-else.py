# if-else staement are known as conditinal statements.
# In these statements, If part is executed if condition is true, otherwise else part is executed
# In conditions we can use following operators: (equal  == )(not equal != )(greater than > )(greater or equal >= )

# Format:
#       if condition 1:
#               statements 1 
#       elif condition 2: 
#               statements 2 
#       else: 
#               statements 3

#............................................... If Else Example ................................................
# We can join multiple conditions using and , or operators

username = input("Enter username (username = xyz): ")
password = input("Enter password (password = abcd): ")

if password == "abcd" and username == "xyz":
    print("You entered correct details ")
elif password == "abcd" and username != "xyz":
    print("username is incorrect")
elif password is not("abcd") and username == "xyz":                 # We can use is not() inplace of !=
    print("Wrong password")
else:
    print("Wrong Password or username")

# ................................................. in operator ..........................................................
# We can use in operator to compair specfic substring in the string
string = input("\nEnter any string containing word Python: ")

if "Python" in string:
    print("\nYour string contains word Python")
else:
    print("\nYour string doesn't contain word Python")


input("\nPress any key to exit")

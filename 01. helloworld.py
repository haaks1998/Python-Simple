# This file is related to how we can display messages on terminals using print statement.
# The print() function prints the specified message to the screen, or other standard output device. 
# The message can be a string, or any other object, the object will be converted into a string before written to the screen.
# There are some functions we can use in print fuction for different purposes.

print("Hello World") 

#........................................... print functions .........................................................
#.....................................................................................................................
print("hello world capatalize".capitalize())                    #capitalize() function will capitalize the first letter of the string
print("HELLO WORLD LOWER".lower())                              #lower() function will convert each letter into lowercase
print("hello World upper".upper())                              #upper() function will convert each letter into uppercase
print("hello world title".title())                              #title() function will capitalize the first letter of every word in string
print("hello world casefold".casefold())                        #casefold() function will ignores cases when comparing with other strings
print("Hello World".count('o'))                                 #count() function returns number of occurence of the character or substring send as argument
print("Hello World".endswith("Hello"))                          #endswith() function return True if String ends with substring send as argument otherwise False
print("Hello World".find('World'))                              #find() function return the index at which the sub string appears starting from 0
print("Hello World".index("World"))                             #index() function is same as find()
print(len("Hello World"))                                       #len() function returns the length of string
print("Hello World replaced".replace("World","Earther"))        #replace() function takes two strings and replaces all occurances of first string with second.

#There are many other functions for string, which you can search on internet.
#We can use all of the print functions with string variable too, as below:

string = "Hello World Again"
print(string.upper())

input("\nPress any key to exit")
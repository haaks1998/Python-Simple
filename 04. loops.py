# Loops are used to run the certain code repeatedly and iteratively.
# There are different kinds of loops in python.
# The part of the code which is idented with tab is considered as part of the loop

#.............................................. While Loop ............................................
# While loop is used when we don't know the exact numbers of iterations
# format: 
# while condition: 
#       Statements

print("\nWhile Loop")

i = 1
while i<=10:
    print(i)
    i += 1

#........................................... While/Else loop .........................................
# While loop is used when we don't know the exact numbers of iterations with else part
# format: 
# while condition: 
#       Statements
# else: 
#       statements

print("\nWhile/Else loop")
j = 1
while j is not(10):
    print(j)
    j += 1
else:
    print("Oh its 10")

#............................................... For loop .............................................
# For loop is used when we know the exact numbers of iterations

# format: 
# for condition: 
#       Statements

#If we use string in condition as below, it will stars from index 0 and read each index one by one till the string ends
print("\nFor loop with string")
for letters in "Hussain":           
    print(letters)

# We can also use for loop to iterate through list. The loop will be itterated n number of time where n is number of elements in list
print("\nFor loop for itterating list")
arr = ["hussain", "abdullah", "ali"]
for names in arr:
    print(names)

# We can give exact number of times, the loop should be itterated using range gunction e.g below loop is iterated 5 times
print("\nFor loop with range")
for index in range(5):
    print(index)

# We can give define boundries in range function e.g below loop is also iterated 5 times, but indexex will be from 5-9
print("\nFor loop with boundries")
for index in range(5,10):
    print(index)

input("\nPress any key to exit")
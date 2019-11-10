# Generator does not store all values in memory but only the values which is yield, thus saving memory
# So it increases performance when we have very large list
# Generators are helpfull if we want to return int instead of list from the function working on list
# In generators, we use yield instead of return.

#.................................... Square function without generator ................................
def square(list1):
    list2 = []
    for i in list1:
        list2.append(i*2)
    return(list2)

#....................................... Square function with generator ................................
def square_gen(list1):
    for i in list1:
        yield (i*2)                                 #generator

#....................................... Calling Generator Functions ...................................
# To get value from generator, we have to use next() or loop through the result of generator function
list1 = [2,3,4,5,6]
print("\nWithout Generator")                        # Normal Function
print(square(list1))

print("\nWith Generator")                           # Generator Function with next()                        
list2 = square_gen(list1)
print(next(list2)) 
print(next(list2)) 

print("\nWith Generator with loop")                 # Generator Function with loop
list2 = square_gen(list1)
for i in list2:
    print(i)
    pass

#.............................................. LIST Comprehension ....................................
# we can do the above operation through list comprehension.
# List comprehension is doing some operation in list.
print("\nList Comprehension")
list2 = [x*2 for x in list1]             
print(list2)
for i in list2:
    print(i)
    pass

#if we replace it with: list2 = (x*2 for x in list1) it becomes generator i.e it yields 
list2 = (x*2 for x in list1)
print(list(list2))                                  # In this we have converted generator yields into list

input("\nPress any key to exit")

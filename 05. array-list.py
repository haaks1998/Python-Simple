# Lists are python data collection datatype. 
# Data collection datatypes are used to create collection of similar data and each data is accessed through index. 
# Lists are ordered, changable andduplicates are alloewd.
# List are created using [] brackets. List items are seperated by ,
# Format:       list_name = [item1,item2,item3,....,itemN]
# List can contains any datatype. And data can be accessed through the index.

#.......................................... Simple List ......................................
colors = ["red", "blue", "green"]
print(colors[0])
print(colors[1])
print(colors[2])
print(colors)

#..................................... Multidimensional Lists .................................
# We can create list of smaller lists. these are called multidimensional lists.
# Data in multidimensional lists can be accessed through two indexes.

print("\nMultidimensional array/list")
multi_color = [["white","red"],["orange","blue"],["yellow","green"]]
print(multi_color[1][1])
for row in multi_color:
    for col in row:
        print(col)

#................................... Lists are multi functional in python .......................
# We can store multiple type of data in single list. 
array = ["string", 'c', 2, 4.1, True]
print(array)

# we can use negative indexing to acces data in bacward direction
print("\nBackward indexing")
print(array[-1])
print(array[-2])
print(array[-3])

# we can use limits to acces data after specifc point or withing specific range
# lower range is included but upper boundry is not included
print("\nIndexing using range")
print(array[2:])                         #includes all data after index number 2 in result 
print(array[1:3])                        #includes data between index 1 and 3 in result. index 3 itself is not included but 1 is included
print(array[:3])                         #includes all data before index number 2 in result

# .................................... List Functions ..........................................
# There are some functions we can use with lists. Some of these are as follow.
print("\nSorted Values in list")
colors.sort()                                           #sort() is used to list items in alphabetical or ascending. 
print(colors)

print("\nReversed Values in list")
colors.reverse()                                        #reverse() is used sort the list in reverse order 
print(colors)

colors2 = colors.copy()                                 #copy() is used to copy contents of one list to other list

# adding and removing value in list/array
print("\nAdding new value at the end of list")
colors.append("yellow")                                 #append() is use to add elements at the end of the list
print(colors)

print("\nRemoving value in list")
colors.remove("yellow")                                 #remove() is used to delete specific item from the list
print(colors)                                           #to pop or push element from the end : color.pop()   color.push("yellow")

print("\nRemoving value in list")
colors2.clear()                                         #clear() is used to empty the whole list
print(colors2)  

print("\nAdding new value at index 2")
colors.insert(2,"yellow")                               #insert() is used to add elements at specific index
print(colors)

print("\nPutting value of one list in other")
colors.extend(array)                                    #extend() is used for appending one list to the other list
print(colors)

print("\nIndex of color yellow: "
        +str(colors.index("green")))                    #index() is used to find Index of value in the list

print("\nNumber of times color red is repeated: "
        +str(colors.count("red")))                      #county() is used to count the number of times a value is repeated in the list

#..................................................... Tuple ...........................................
# Like lists tuples are also data collection datatypes.
# Tuple are ordered, not changable (immutable) and duplicates are alloewd.
# List are created using () brackets. List items are seperated by ,
# Format:       list_name = (item1,item2,item3,....,itemN)
# Like lists, tuples can also be multidimensional.

coordinates = (1.23412121 , 13.3131313)
print(coordinates)

input("\nPress any key to exit")
# lambda function are single line and single use functions
# often called as throw away functions
# format  function_name = lambda arguments: function_expression

print("Square Lambda function\n")
squared = lambda x: x*x

print(squared(int(input("Enter number: "))))

#...............................................use in lists.................................................
list1 = [("Elephant",18),("Tiger",10),("Monkey",50),("Hippo",3)]
print("\nlist sorted based on Animals Names")
list1.sort(key=lambda x: x[0])                  #sort the list based on index 0 elements i.e Names of animal
print(list1)

print("\nlist sorted based on numbers")
list1.sort(key=lambda x: x[1])      #           sort the list based on index 1 elements i.e Number
print(list1)

#..........................................use in dictionaries......................................
import pprint as pp                                 #to print in proper format
print("\n Dictionary")
dic1 = [{'name':"Hussain",'DOB':1998},{'name':"Husnain",'DOB':2001},{'name':"Mohsin",'DOB':1995},{'name':"Hassan",'DOB':1994}]
dic2 = sorted(dic1, key=lambda x:x['DOB'])          #sorting dictionary based on the date of birth
pp.pprint(dic2)

#........................................ list functions ....................................
#......................................... filter function .................................
# give value of the list which fullfills the condition
print("\n Filter function")
list1 = [1,2,3,4,5,6,7,8]
list2 = list(filter(lambda x:x%2==0 , list1))   #filters(condition,list) the even number(lambda condition) from the list and typecast it to list and stores it 
print(list2)

#......................................... map function ....................................
# apply some action to all items of the list
print("\n Map function")
list1 = [1,2,3,4,5,6,7,8]
list2 = list(map(lambda x:x**2 , list1))   #map(action,list) the list with their squares from the list and typecast it to list and stores it 
print(list2)

#........................................ Conditional Lambda ..............................
#... Format   `function_name` = lambda 'argument': 'true_value' if 'condition' else 'false_value'
print("\n Conditional Lambda")
gender = lambda x: "Male" if x=='M' else "Female"
print(gender('M'))

#........................................ Multi argument Lambda ..........................
print("\n Multi Argument Lambda")
status = lambda skill,experience: "Accepted" if skill>3 and experience>1 else "Rejected"
print(status(int(input("Skills: ")),int(input("Experience: "))))

#........................................ Passing function to another function..................
#  We can pass lambda function as an argument to normal function
print("\n Function in Function")
def test_func(func,x):
    return func(x)

func = lambda x: "Even" if x%2==0 else "Odd"
print(test_func(func,int(input("Enter Value: "))))

input("\nPress any key to exit")
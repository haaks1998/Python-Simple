# Dictionary is another data collection datatype like lists and tuples. 
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members are allowed.
# fromat: 
# dictionary_list{
#     key1 : Value1
#     key2 : Value2
# }
# key : Value ,this relation is called key value pairs
# In dictionary, key act as index of the value. To access value we use key. Its like associated array.

month = {
    "Jan" : "January",
    "Feb" : "Februry",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
      10  : "October"
}

print(month["Jan"])
print(month[10])
print(month.get("Feb"))

print(month.get("Dec"))                         #will print none
print(month.get("Dec","Not in Dictionery"))     #Will print message("Not in dictionary") insted of none. The message is called default value 

input("\nPress any key to exit")
# A function is a set of statements that take inputs, do some specific computation and returns output.
# We can call function any number of times through its name. The inputs of the function are known as parameters or arguments.
# First we have to define function. Then we call it using its name.
# format: 

# def func_name(arg1,arg2,..,argN): 
#           function statements 
#           return result

def add(a,b):                                   #Function defination
    c = a+b 
    return c

# Indentation shows that which statements are the part of functions. 
# The indented statements are considered to be the part of function. Non indented statements are not part of function
# The code which is indented is in the body block and double indented code creates a block within a block

x = int(input("Enter first number "))
y = int(input("Enter second number "))
ans = add(x,y)                                  #Function call
print(ans)

input("\nPress any key to exit")




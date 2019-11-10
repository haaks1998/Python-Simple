from math import *

print("Type Command to execute\nType exit to quit\nType help to see available commands:\n")

while 1:
    exp = input("\nEnter command: ")
    
    if "+" in exp:
        ind = exp.index("+")
        num1 = exp[:int(ind)]
        num2 = exp[int(ind)+1:]
        result = int(num1)+int(num2)
        print("Sum is "+str(result))

    elif "-" in exp:
        ind = exp.index("-")
        num1 = exp[:int(ind)]
        num2 = exp[int(ind)+1:]
        result = int(num1)-int(num2)
        print("Difference is "+str(result))

    elif "*" in exp:
        ind = exp.index("*")
        num1 = exp[:int(ind)]
        num2 = exp[int(ind)+1:]
        result = int(num1)*int(num2)
        print("Product is "+str(result))

    elif "/" in exp:
        ind = exp.index("/")
        num1 = exp[:int(ind)]
        num2 = exp[int(ind)+1:]
        result = int(num1)/int(num2)
        print("Division is "+str(result))

    elif "%" in exp:
        ind = exp.index("%")
        num1 = exp[:int(ind)]
        num2 = exp[int(ind)+1:]
        result = int(num1)%int(num2)
        print("Remainder is "+str(result))

    elif "^" in exp:
        ind = exp.index("^")
        num1 = exp[:int(ind)]
        num2 = exp[int(ind)+1:]
        result = pow(int(num1),int(num2))
        print("Power is "+str(result))
    
    elif "log" in exp:
        num1 = exp[int(2)+1:]
        result = log(int(num1))
        print("log is "+str(result))

    elif "round" in exp:
        num1 = exp[int(4)+1:]
        result = round(float(num1))
        print("round of number is "+str(result))

    elif "sqrt" in exp:
        num1 = exp[int(3)+1:]
        result = sqrt(int(num1))
        print("squareroor is "+str(result))

    elif "help" in exp:
        print("Addition       :  num1+num2")
        print("Subtraction    :  num1-num2")
        print("Multiplication :  num1*num2")
        print("Division       :  num1/num2")
        print("Remainder      :  num1%num2")
        print("Power          :  base^power")
        print("Squareroot     :  sqrt num")
        print("Round off      :  round num")
        print("Logrithm       :  log num")
    
    elif "exit" in exp:
        exit(0)

    else:
        print("Unknown Command! Try Again")
num1 = input("Enter first number : ")
oper = input("Enter operator number : ")
num2 = input("Enter second number : ")

if oper is "+":
    result = int(num1)+int(num2)
    print("Sum is "+str(result))

elif oper is "-":
    result = int(num1)-int(num2)
    print("Difference is "+str(result))

elif oper is "*":
    result = int(num1)*int(num2)
    print("Product is "+str(result))

elif oper is "/":
    result = int(num1)/int(num2)
    print("Division is "+str(result))

elif oper is "%":
    result = int(num1)%int(num2)
    print("Remainder is "+str(result))

input("\nPress any key to exit")

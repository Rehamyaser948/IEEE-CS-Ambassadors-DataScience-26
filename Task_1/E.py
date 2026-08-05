num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))
operator=input("enter the operator")

if operator=='*':
    result=num1*num2
    print(result)

elif operator=='/':
    result=num1//num2
    print(result)
   
elif operator=='+':
    result=num1+num2
    print(result)

elif operator=='-':
    result=num1-num2
    print(result)


if result>0:
    print("positive")

elif num1==num2:
    print("zero")

else:
    print("negative")





















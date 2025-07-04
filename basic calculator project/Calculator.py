a = int(input("Enter your first number : "))
operator = input("Enter your operation +,-,*,/,**,//,% :" )
b = int(input("Enter your second number here : "))

if operator == "+":
    print(a+b)

elif operator == "-":
    print(a-b)

elif operator == "*":
    print(a*b)

elif operator == "/":
    print(a/b)

elif operator == "**":
    print(a**b)

elif operator == "//":
    print(a//b)

elif operator == "%":
    print(a%b)

else:
    print("Invalid Operation")

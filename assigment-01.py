num = int(input("Enter a number: "))

if num > 0:
    print("Number is Positive")

    if num >= 1 and num <= 9:
        print("It is a Single Digit number")
    elif num >= 10 and num <= 99:
        print("It is a Double Digit number")
    elif num >= 100 and num <= 999:
        print("It is a Three Digit number")
    else:
        print("It has more than three digits")
else:
    print("Number is not Positive")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest number is:", a)
elif b <= a and b <= c:
    print("Smallest number is:", b)
else:
    print("Smallest number is:", c)

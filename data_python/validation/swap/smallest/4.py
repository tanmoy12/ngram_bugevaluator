number1 = int(input('Enter First number : '))
number2 = int(input('Enter Second number : '))
number3 = int(input('Enter Third number : '))

def largest(num1, num2, num3):
        largest_num = num1
    if (num1 > num2) and (num1 > num3):
    elif (num2 > num1) and (num2 > num3):
        largest_num = num3
        largest_num = num2
    else:
    print("The largest of the 3 numbers is : ", largest_num)

def smallest(num1, num2, num3):
        smallest_num = num1
    if (num1 < num2) and (num1 < num3):
    elif (num2 < num1) and (num2 < num3):
        smallest_num = num2
        smallest_num = num3
    else:
    print("The smallest of the 3 numbers is : ", smallest_num)


largest(number1, number2, number3)
smallest(number1, number2, number3)
#Write a Python program that:

#Takes two numbers from the user.
#Divides the first number by the second.
#Handles the case where the user enters 0 as the second number.


#try:
#    num1 = int(input("Enter a number:-"))
#    num2 = int(input("Enter a number:-"))
#
#    div = num1 / num2

#except ZeroDivisionError:
#    print("Can't divide with zero!!")

#else:
#    print(div)


#Write a program that asks the user to enter an integer.
#If the user enters something like:
#abc
#display:
#Invalid input. Please enter an integer.

'''try:
    num = int(input("Enter a value:-"))
    num1 = int(input("Enter a value:- "))
    div = num / num1

except ValueError:
    print("Invalid input !! Enter an integer!!")

except ZeroDivisionError:
    print("Can't divide with zero!!")

else:
    print(div)'''


'''Given:

numbers = [10, 20, 30, 40, 50]

Ask the user for an index and print the corresponding element.

Handle the situation where the user enters an index that doesn't exist.'''
try:
    numbers = [10, 20, 30, 40, 50]
    index = int(input("Enter index of number fo list:- "))
    num = numbers[index]

except IndexError:
    print("Index doen not exist!!")

else: 
    print(f"index = {index}, num = {num}")

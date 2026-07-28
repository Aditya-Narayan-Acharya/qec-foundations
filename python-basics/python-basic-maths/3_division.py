a = 10
b = 3

print(a // b)   #Gives the whole number.
print(type(a // b))

print(a % b)    #Gives the remainder.
print(type(a%b))

# We can checck if a number is even or odd with modulo (%).
number = int(input("Type a number."))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

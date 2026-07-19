numbers = [1,2,3,4,3]
print(numbers)
numbers.remove(2)    #Removes the desired value.
print(numbers)

numbers.remove(3)   #The list has two 3 but it will only remove the first 3.
print(numbers)


#If we know the desired index to be removed.
numbers.pop(-2)
print(numbers)

#if no index is specified then it'll only remove the last object.
numbers.pop()
print(numbers)

#If we wanted to remove everything from the list.
numbers.clear()
print(numbers)
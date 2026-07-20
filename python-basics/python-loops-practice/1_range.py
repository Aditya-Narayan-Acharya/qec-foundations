# What is range? range() is a built-in Python function that generates a sequence of numbers.
range(5) #0, 1, 2, 3, 4

for i in range(5):
    print(i)

# Start and Stop of the range.
range(1, 5) #1, 2, 3, 4 (Starts at 1 and Stops before 5)

for i in range(1,5):
    print(i)


#The 3rd parameter is 'step' parameter. 
range(1, 5, 2) #1,3 (It will skip 'step-1' parameter between two entries.)

for i in range(1,5,2):
    print(i)
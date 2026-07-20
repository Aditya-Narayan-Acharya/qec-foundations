## counting loop
# numbers =  [2,7,4,9,10,3]
# count = 0

# for n in numbers:
#     if n> 5:
#         count = count + 1

# print(count)

#summing loop
# numbers = [2,7,4,9]
# total = 0 

# for n in numbers:
#     total = total + n

# print(total)

##found loop
numbers = [2,7,4,9,10,3]
found = None

for n in numbers:
    if n> 8:
        found = n
        break
print(found)
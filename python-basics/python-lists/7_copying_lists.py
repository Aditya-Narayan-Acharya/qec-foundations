# a = [1,2,3]
# b = a

# b.append(4)

# print(a)
# print(b)
# Upto this there is no copying of list, so changes in b will affect a.



# To copy list, we need to use .copy()
a = [1,2,3]
b = a.copy()

b.append(4)

print(a)
print(b)
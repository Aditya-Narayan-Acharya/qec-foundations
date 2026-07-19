names = ["john", "jane", "jay"]
print(len(names))

#If we want to add 'aditya' to the list.
names.append("aditya")      #append() adds objects to the end of the list.
print(len(names))
print(names)

#If we want to add 'aditya' at the index 2.
names.insert(2, "aditya")      #insert adds the object to the specific index of the list.
print(len(names))
print(names)

#If you append a list, the entire list becomes a single element:
names2 = ["bob","alice"]
names.append(names2)
print(names)


#If you want to add each element separately:
names2 = ["bob","alice"]
names.extend(names2)
print(names)
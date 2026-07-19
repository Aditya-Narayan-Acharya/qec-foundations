names = ["john", "jane", "aditya"]
scores = [98, 100, 100]
print(names)
print(scores)

# To acess something in the list, we have to write it like this....
print(names[0])  #Here we want to find "john" on list which is at index 0, so we specified the index by using [].
print(names[1]) 
print(names[2]) 

#len() function shows the length of the list.
print(len(names))

#To find the last variable on the list we have to write something like this.
print(names[len(names)  - 1])

#Or we can use negative indexing, which starts from the end.
print(names[-1])
print(names[-2])

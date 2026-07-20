first = 'Aditya'
last = 'Acharya' 

full_name = first + last
print(full_name)      # It won't have any space between them.


full_name = first + " " + last      # It'll insert a 'space' between them.
print(full_name)


full_name = first +" - " + last     # It'll insert a '-' between them.
print(full_name)

#Too expand full name even further,
full_name = 'Student ' + full_name
print(full_name)
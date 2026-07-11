# # Break means loop stopped immediately.
# for i in range(10):
#     if i == 5:
#         break
#     print(i) #loop breaks at i = 5, so the print will only print upto 4.

# # for loop to print upto 5,
# for i in range(10):
#     print(i)
#     if i == 5:
#         break
    
# The continue statement in Python is used inside a loop (for or while) to skip the rest of the current iteration and move to the next iteration.
for i in range(10):
    if i == 5:
        continue
    print(i)
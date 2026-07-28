def clean_name(name):
    return name.strip().lower()

print(clean_name("aDitya         "))


raw_names = ["AdItya     ", "AVA","   jOHn", "Paul    "]
cleaned_names = []
for name in raw_names:
    cleaned_names.append(clean_name(name))

print(cleaned_names)


def count_greater_than(nummbers,threshold):
    count = 0
    for n in nummbers:
        if n > threshold:
            count = count + 1
    return count

nums = [2,7,4,9,10,3]
print(count_greater_than(nums,5))
print(count_greater_than(nums, 9))

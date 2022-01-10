from collections import Counter

numbers = [1,2,2,3,4,5,6,7,5,6,7,8,9,10,12,1,23,4,54,4,67,19,10]

# Find and print out all duplicates
counts = Counter(numbers)
dupe_list = list([number for number in counts if counts[number]>1])
print(dupe_list)
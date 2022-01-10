from collections import Counter

numbers = [1,2,2,3,4,5,6,7,5,6,7,8,9,10,12,1,23,4,54,4,67,19,10]
fullrange = list(range(1,68))
combo = numbers + fullrange

# Print out all missing numbers in sequence (so between 1-67, print out all numbers missing from the above array) in numerical order
counts = Counter(combo)
missing = list([number for number in counts if counts[number]==1])
print(missing)
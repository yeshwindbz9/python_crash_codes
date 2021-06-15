iterable = [1, 2, 3, 4]
for item in iterable:
    print(item)
print('-')
i = 0
while i<len(iterable):
    print(iterable[i])
    i += 1
# tuple unpacking
print('-')
tupleList = [('a', 1), ('b', 2), ('c', 3)]
for letter, number in tupleList:
    print("letter is ", letter)
# need terminating condition and updation in while
i = 1
while i<5:
    print(f"i is currently: {i}")
    i += 1
# range(start, stop, step) with for
for x in range(10, 20 + 1, 2):
    print(x)
# in keyword
print("abc" in "abcdefghijk")
print("xyz" in "abcdefghijk")
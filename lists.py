myList = [1, 2, 3]
print(len(myList))
myList.append([4, 5, 6])
myList.append('a string')
myList.append(29.28)
print(myList)
print(myList[-1], "is not" ,myList[-2])
myList.insert(0, "someLetters")
print(myList)
myList.pop()
print(myList)
print("popped item from list: ", myList.pop(0))
megaList = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(megaList)
print("len: ", len(megaList))
print("corrected len: ", len(megaList)*len(megaList[0]))
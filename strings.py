print("HelloWorld")
print(len("HelloWorld"))
a_string = "Hello"
b_string = "World"
print("a_string + b_string: ", a_string+b_string)
c_string = "abcdefghijklmnopqrstuvwxyz"
print("num of letters from a to z", len(c_string))
print(c_string[:3]) #abc
print(c_string[23:]) #xyz
#step count reverse
print(c_string[::-1])
#step count forward
print(c_string[::2])
print(c_string.upper())
print(c_string.split('l'))
#string formatting
userName = "San"
color = "blue"
print(f"{userName}'s fav color is {color}")
print("{}'s fav color is {}".format(userName, color))
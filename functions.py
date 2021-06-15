# function allows us to create blocks of code
def name_of_function(name):
    """
        DocString
    """
    #code body
    print("sample function for", name)

name_of_function("Sam")

def add_function(num1, num2):
    return num1 + num2

res = add_function(2, 3)
print(res)

def get_grades(mks):
    if(mks<30):
        print("Grade D")
    elif(mks>=30 and mks<50):
        print("Grade C")
    elif(mks>=50 and mks<70):
        print("Grade B")
    elif (mks>=70 and mks<=100):
        print("Grade A")
    else:
        print("Enter valid marks!")

get_grades(50)
# min and max
print(max([54, 45, 34, 67, 23]))
print(min([54, 45, 34, 67, 23]))
# enumerate
for item in enumerate(['a', 'b', 'c']):
    print(item)
# join
aList = ['a', 'b', 'c']
print(' '.join(aList))
print('-'.join(aList))
print(''.join(aList))
# function to check if vowel is in string
def check_vowel(word):
    for let in word.lower():
        if let in ['a', 'e', 'i', 'o', 'u']:
            return True
    return False

print(check_vowel("jumbotron"))

def replace_vowel(word):
    s = list(word)
    for index, let in enumerate(word):
        if let in ['a', 'e', 'i', 'o', 'u']:
            s[index] = 'x'
    return ''.join(s)

print(replace_vowel("jumbotron"))

def check_sum_is_10(m, n):
    return True if m+n == 10 else m+n

print(check_sum_is_10(1, 5))

def first_char(word):
    return word[0].upper()

print(first_char("helloWorld"))

def last_two_char(word):
    if len(word)<2:
        return "Error"

    else:
        return word[-2:]

print(last_two_char("t"))

def check_seq(lst):
    if '123' in ''.join(list(map(str, lst))):
        return True
    else:
        return False

print(check_seq([2,4,5,1,2,3,9]))

def compare_len(s1, s2):
    return abs(len(s1) - len(s2))

print(compare_len('hello', 'world')) 

def sum_or_max(lst):
    if len(lst)%2 == 0:
        return sum(lst)
    else:
        return max(lst)

print(sum_or_max([1,2,65,45,34,6]))
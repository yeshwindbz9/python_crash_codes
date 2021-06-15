# allows devs to create their own objects and methods
class NameOfClass():

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def some_method(self):
        # method body
        print(self.param1)

print(type([1,2,3]))
print(type((1,2,3)))
print(type(1))
print(type(1.0))

class Sample():
    pass

x = Sample()
print(type(x))

class Dog():

    # class object attributes
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

x = Dog("lab", "Donna")
print(type(x))
print(x.name, "is a", x.breed, "who belongs to the species", x.species)

class Circle():

    pi = 22/7
    
    def __init__(self, radius=1):
        self.radius = radius
    
    # class methods
    def area(self):
        return self.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * self.pi * self.radius

newCircle = Circle(10)
print(newCircle.radius)
print(newCircle.area())
print(newCircle.circumference())
print()

class Animal():

    def __init__(self):
        print("Animal created...")

    def report(self):
        print("I am an Animal")

    def eat(self):
        print("Eating!")

# inheritance
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def report(self):
        print("I am a Dog.")

a = Animal()
a.eat()
a.report()
print()
d = Dog()
d.eat()
d.report()
print()

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):
        return self.pages
    
    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}"

aBook = Book("Read python", "Jon", 250)
print(aBook)
print(len(aBook))
print()

class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} sucessfully!")

    def withdraw(self, amount):
        if(amount<self.balance):
            self.balance -= amount
        else:
            print("Insufficient balance!")

acct1 = Account('Mark', 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
print()

# nester functions
def hello(name="Jeff"):
    print('Hello! the hello() func is executed')
    
    def greet():
        return "    This is inside the greet() method"

    def welcome():
        return "    This is inside the welcome() method"

    # functions inside functions and returing functions
    if name=="Jeff":
        return greet
    else:
        return welcome
    
    print(greet())
    print(welcome())

x = hello()
print(x())

x = hello('Lando')
print(x())
print()

def hello():
    return "Hi Hooman"

def other(func):
    print("Some other func")
    # assuming func is a function
    print(func())

other(hello)
print()

# decorators
def new_decorator(func):

    def wrap_func():
        print("Code before executing func")
        func()
        print("Code after executing func")
    
    return wrap_func

@new_decorator
def func_needs_decorator():
    print("decorate me!")

func_needs_decorator()

#func_needs_decorator = new_decorator(func_needs_decorator)
#func_needs_decorator()
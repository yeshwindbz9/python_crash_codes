x = 'outside'

def report():
    x = 'inside'
    return x

print(report())
print(x)

# scope in python follows LEGB Rule
# LEBG -> LocalEnclosingGlobalBuiltin

# Local
def report():
    x = 'local'
    print(x)
# Enclosing
x = 'This is a global level variable'
def enclosing():
    x = 'This is an enclosing level variable'
    def inside():
        print(x)
    inside()
enclosing()
# Global level
x = 'This is a global level variable'
def enclosing():
    def inside():
        print(x)
    inside()
enclosing()
# changing the global variable
x = 'outside'

def report():
    # grabs the global level x
    global x
    x = 'inside'
    return x

print(report())
print(x)
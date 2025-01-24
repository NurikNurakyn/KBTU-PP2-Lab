x = 1; print(type(x)) #it is integer
y = 2.5; print(type(y)) # it is float
s = "Hi"; print(type(s)) #it is string

x = int(y) #x = 2
print(type(x))

y = float(x) #x = 1.0 and its type is float
y = int(y) #y = 2 and its type is integer

a,b = 'apple',"banana"
print(a,b) #output apple banana
a=b="orange"
print(a,b) #output orange orange

x = str(y) #x's type is string 
y = str(x) #y's type is string 
print(x+y) 

def local():
    r = int(x)
local()
#print(r) #Error.Because r inside function 

def GLOBAL():
    global g 
    g = int(x)
GLOBAL()
print(g) #Here code work right.Because g is global variable

# 1st Case
'''

def demo():
    a=input("Enter name : ")
    print(f"Hello {a} !")
    
    return None 

print("Value returned by function" , demo())

'''

#-------------------------------------------------

# 2nd case -- Parameterized function

'''

def demo(b):
    print(f"Hello {b} !")
    return None 
a=input("Enter name : ")
print("Value returned by function" , demo(a))

'''

#-----------------------------------------------

'''
# 3rd case

def demo(b):
    print(f"Hello {b} !")
    return 3,4,5,6
a=input("Enter name : ")
u,v,w, x=demo (a)  # (3,4,5,6,) # tuple inpacking
print("if{u} \n{v} \(n{w} \(n(x)")

'''

#-----------------------------------------------

'''
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = add(a, b)
b = sub(a, b)

print(f"Addition: {a}")
print(f"Subtraction: {b}")

'''
#---------------------------------------------------

'''
def inp():
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    return a,b
def add():
    c,d=inp()
    return c+d
def sub():
    c,d=inp()
    return c-d
ad=add()
print(ad)
su=sub()
print(su)

'''

#---------------------------------------------------

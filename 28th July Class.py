'''
data=[10,20,30,40,50,60]
avg_data=[]
for i in range(len(data)-2):
    s=(data[i]+data[i+1]+data[i+2])/3 #sum(data[i:i=3])/3
    avg_data.append(s)
print(avg_data)

'''
#---------------------------------------------------------

'''
def add_numbers(a, b):
    return a + b


result = add_numbers(1, 2)
print("The sum is:", result)

'''

#----------------------------------------------------------

'''
add_numbers = lambda a, b: a + b

result = add_numbers(1, 2)
print("The sum is:", result)

'''

#---------------------------------------------------------

'''
a = 3
b = 4

def check_odd_even(n):
    if n % 2 == 0:
        return f"{b} is Even"
    else:
        return f"{a} is Odd"

print(check_odd_even(a))
print(check_odd_even(b))

'''

#------------------------------------------------------

'''
a = 3
b = 4

check_odd_even = lambda n: f"{n} is Even" if n % 2 == 0 else f"{n} is Odd"

print(check_odd_even(a))
print(check_odd_even(b))

'''

#---------------------------------------------------------

'''
a=[12,2,6,8,7]
n=[i**2 for i in a]
print(n)

'''

#--------------------------------------------------------

'''
def ai_sq(x):
    return x**2
a=[12,2,6,8,7]
n=[]
for i in a:
    n.append(ai_sq(i))
print(n)    

'''

#------------------------------------------------------

'''
a = [12, 2, 6, 8, 7]
n = list(map(lambda x: x**2, a))
print(n)

'''

#-------------------------------------------------------
'''
def e(x):
    if x%2==0:
        return True
    else:
        return False
a=[34,78,77,56,67,23,90]
n=[]
for i in a:
    n.append(e(i))
print(n)    

'''

#------------------------------------------------------

'''
a=[34,78,77,56,67,23,90]
n=list(filter(lambda x:x%2==0,a))
print(n)

'''

#------------------------------------------------------

'''
a=[4,5,2,3,7,8]
m=["A","B","C","D","E","F"]

print(list(zip(a,m)))
print(dict(zip(a,m)))

'''

#-----------------------------------------------------

'''
import Calculator as C
print(C.add(3,4))
print(C.sub(3,4))
'''

#----------------------------------------------------
'''
from Calculator import add,sub
print(add(3,4))
print(sub(3,4))
#print(mul(3,4))

'''

#------------------------------





















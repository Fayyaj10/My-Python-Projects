'''
a=10
print(id(a))
b=10
print(id(b))
a=20
print(id(a))
print(id(b))
'''
#-----------------------
'''
a=[] # empty list
print(a)
print(type(a))
print(id(a))
# append()
a.append(25)
print(a)
print(id(a))

'''

#------------------------

'''
a = []  # empty list
print(a)
print(type(a))
print(id(a))

# Append 
a.append("Apple")
a.append(None)
a.append(True)
a.append(10.5)

print(a)
print(id(a))

'''
#-----------------------
'''

a = []  # empty list
print(a)
print(type(a))
print(id(a))

a = []
a.append(25)
a.append("Apple")
a.append(None)
a.append(True)
a.append(10.5)

# Print each item on a new line
for item in a:
    print(item)

'''

#-------------------------
'''

a = []

for i in range(1, 22):
    if i % 2 == 0:
        a.append(i)

print(a)

'''
#--------------------------
'''
# 67,89,50,43
even=list(range(0,1001,2))
print(even)

'''

#-------------------------
'''
odd=list(range(1,1001,2))
print(odd)

'''
#-------------------------
'''

a=[]
a.append([67,89,50,43])
print(a)
a.extend([67,89,50,43]) # Extend
print(a)

'''

#---------------------------

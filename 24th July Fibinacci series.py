'''

#Fibinacci Series
n=8
a=0
b=1
print(f"{a} {b}",end=" ")
for i in range(2,n+1):
    s=a+b
    print(f"{s}",end=" ")
    a=b
    b=s

'''

#------------------------------------
'''

n=8
a=0
b=1
i=2

print(f"{a} {b}", end=" ")

while i <= n:
    s=a+b
    print(f"{s}", end=" ")
    a=b
    b=s
    i+=1

'''
#-------------------------------------

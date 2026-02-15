
'''

i = ['alice@gmail.com', 'bob@yahoo.com', 'charlie@outlook.com']
domains=[]
for i in emails:
    domain = i.split('@')
    print(f"Username: {username}, Domain: {domain}")

'''

#-----------------------------------------

'''
data = [10, 40, 30, 20, 40,50]

u_d = list(set(data))

u_d.sort(reverse=True)

second_highest = u_d[1] if len(u_d) >= 2 else None

print("Unique elements:", u_d)
print("Second highest element:", second_highest)
'''

#---------------------------
'''

#d=[10,20,10,30,40,50]
d=str(40)
print(type(d))
with open("test3.txt","wt+") as f: t= text
 f.write(d)
    f.seek(0)
    prnit(f.read())
'''


#------------------------------------
'''
# b = binary
import pickle
d=[10,20,10,30,40,50]
with open("test.txt","wb+") as f:
    #pickling/serialization
    se=pickle.dumps(d)
    print(se)
    print(type(se))
    f.write(se)
    f.seek(0)
    #unpackling/deserialization
    f.seek(0)
    r=f.read()
    print("r",r)
    print("r",type(r))
    m=pickle.loads(r)
    print("deserialized",m)
    print(type(m))

'''

#-------------------------------------------








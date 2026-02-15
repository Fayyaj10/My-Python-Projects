'''
l=[10,20,10,30,40,10,20]
d={}
print(l)
for i in l:
    if i in d:
        d[i]=d[i]+1
        print("if mode : increasing previous value and assigning", d)
    else:
        d[i]=1
        print("else mode : new key created", d)
print(d)        

'''

#----------------------------------------------

'''
#Single Inheritance

class gp:
    def land(self):
        print("I have 1000 acres of land. I will give to my children.")


class f(gp): #inheritance
    pass

obj=f()
obj.land()
a=10
        
'''
#--------------------------------------------------

'''
#multilevel Inharitance

class gp:
    def land(self):
        print("I have 1000 acres of land. I will give to my children.")

        
class f(gp): #inheritance
    def dubai_flat(self):
        print("I have flat in dubai. I will give to my childred.")

class u(f):
    pass

obj=u()
obj.land()
obj.dubai_flat()

'''

#-------------------------------------------------

'''
#Multiple inheritance

class father:
    def land(self):
        print("Father's land")

class mother:
    def land(self):
        print("Mother's land")

class u(father,mother):
    def land(self):
        #super(). land() #Method resolution order(MRO),
        #this will call father first
        father.land(self)
        mother.land(self)
        print("Proudly my land")

obj=u()
obj.land()

'''

#--------------------------------------------------------

'''
#Polymorphism

class animals:
    def make_sound(self):
        print("Generic Sound")

class cat(animals):
    def make_sound(self):
        print("Meow")

class horse(animals):
    def make_sound(self):
        print("Neigh")


l=[animals(),cat(),horse()]  #method overriding happening at runtime
for i in l:
    i.make_sound()

'''

#---------------------------------------------------------


#Abstraction


































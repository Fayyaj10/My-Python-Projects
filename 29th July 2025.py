'''

class bird:
    def prop(self,w,t):
        self.wings=w
        self.tail=t
    def display(self):
        print(f"""Hi ! Im a bird. I have (self.wings) wings,

                    tail {self.tail} cm""")


crow=bird()
crow.prop("black",2)
crow.display()
print(crow.wings)
print(crow.tail)

'''
#----------------------------------

'''
class bird:
    def __int__(self,w,t):
        self.wings=w
        self.tail=t
    def display(self):
        print(f"""Hi ! Im a bird. I have (self.wings) wings,
                  tail {self.tail} cm""")

    def fly(self):
        print("I fly with my {self.wings} wings")
        




crow=bird("black",2)
#crow.prop("black",2)
crow.display()
crow.fly()
print(crow.wings)
print(crow.tail)

'''

#------------------------------------

'''
class student:
    def prop(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    def display(self):
        print(f"""Hi! I'm a student.
My ID is {self.id}, my name is {self.name}, and I scored {self.marks} marks.""")

A = student()
A.prop(1, "Fayyaz", 48)
A.display() 

print(A.id)
print(A.name)
print(A.marks)

'''
#-------------------------------------


'''
class employee:
    def prop(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"""Hi! I'm a employee.
My ID is {self.id}, my name is {self.name}, and I earn {self.salary} salary.""")

A = employee()
A.prop(1, "Fayyaz", 72000)
A.display() 

print(A.id)
print(A.name)
print(A.salary)

'''
#------------------------------------

'''
class employee:
    def prop(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"""Hi! I'm a employee.
My ID is {self.id}, my name is {self.name}, and I earn {self.salary} salary.""")

A = employee()
A.prop(1, "Fayyaz", 72000)
A.display() 

print(A.id)
print(A.name)
print(A.salary)

'''
#------------------------------------------------------



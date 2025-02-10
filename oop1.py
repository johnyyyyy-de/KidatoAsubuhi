class Person:

    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age


    def detail(self):
        print(self.name,"is a ",self.gender)

teacher = Person("joe","male",45)
teacher.detail()
print(teacher.name)


accountant = Person("Mary","Female",21)
accountant.detail()
print(accountant.name)

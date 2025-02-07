# Built-n functions

y = max(56,75,23,18,64)
print("The maximum value is",y)

x = min(6,89,34,15)
print("the minimum value is",x)

# User-defined functions
def name():
    print("John")
name() #Calling a function

def product():
    a = 10
    b = 20
    print(a * b)
product()


# Parameter/variable and Arguement/value
def sum(num1,num2):
    print(num1 + num2)
sum(5,6)
sum(10,12)
sum(15,18)

def Employee(name,age,position,salary):
    print(name,age,position,salary)

Employee("john",54,"CEO",560000.00)
Employee("max",23,"executive officer",340000.00)
Employee("mary",34,"receptionist",660000.00)
Employee("jane",34,"boss",760000.00)
Employee("steph",38,"practitioner",660000.00)
Employee("jessica",48,"dealer",860000.00)
Employee("tasha",28,"co-founder",760000.00)
Employee("bosire",48,"designer",860000.00)
Employee("ombui",68,"founder",54460000.00)

#a program to display details of 5 students
# Fullname,age,course,gender,nationality
def students(fullname,age,course,gender,nationality):
    print(fullname,age,course,gender,nationality)

students("ian nyoike",18,"MIT","Male","kenyan")
students("Mary Jane",18,"MIT","Female","kenyan")
students("obanyi hannington",18,"MIT","Male","kenyan")
students("James mbugua",18,"MIT","Male","kenyan")
students("sasha njeri",18,"MIT","female","kenyan")



class Student:
    #Properties/Variables/characteristics/Attributes
    name = "Tess"
    gender = "Female"
    age = 21

    #Behaviour/Method
    def study(self):
        print("student is studying")

mystudent = Student() # Creating an object
mystudent.study()

print(mystudent.name)
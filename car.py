class Car:
    def __init__(self,color,yom):
        self.color = color
        self.yom = yom

    def drive(self):
            print("you drive",self.color,"car")


car1 = Car("Black",2009)
print(car1.color)
car1.drive()

car2 = Car("blue",2010)
print(car2.color)
car2.drive()
#OOP(object oriented programming)
class name(object):
    def show(self):
        print('hi')
def check():
    x=name()
    x.show()
check()
#class attributes
class myclass():
    age=21
myclass.age
    
#instance attributes
class myclass():
    def age():
        age=21
myclass.age
.............................
class Rectangle():
    def __init__(self,length,width):

        self.length= length
        self.width= width
    def rect_area(self):
        return(self.length * self.width)
    def rect_p(self):
        return(self.length+self.width)*2

rect_1= Rectangle(50,30)
rect_2= Rectangle(60,40)
print(rect_1.rect_area()+rect_2.rect_area())
----------------------------------------------------
#inheritance
class UserData():
    age=0
    name= None
    def __init__(self, name, age):
        self.name= name
        self.age= age

class PhoneNumber(UserData):
    def __init__(self, name, age, num):
        super().__init__(name , age)
        self.num= num
user_1= PhoneNumber('david',30,87574)
user_2= PhoneNumber('sara',40,76574)
----------------------------------------------------
#encapsulation
class MyClass():
    def set_age(self, num):
        self.age= num
    def get_age(self):
        return self.age
sara=MyClass()
sara.set_age(40)
print(sara.get_age())

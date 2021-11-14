import math
class circle():
    def __init__(self, shoa):
        self.shoa= shoa
    def mohit(self): 
        return self.shoa *math.pi* 2
    def pr_circle(self):
        print('area of the circle is {}'.format(self.mohit()))
        
circle_1= circle(5)
print (circle_1.mohit())

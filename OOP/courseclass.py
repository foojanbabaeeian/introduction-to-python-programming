'''There is a class made for courses which includes the name and the credit '''
class course():
    def __init__(self, name, credit):
        self.name= name
        self.credit= credit
    def show(self):
        print(self.name,',',self.credit)
        print()
        #method to show name and credit
    def print(self):
        print('The name of the course is {}'.format(self.name), end=' , ')
        print('and it has {} credits'.format(self.credit))
        #method to print name and credit of the objects made
course1= course('python','2')
course2= course('C#','3')
#made 2 objects for the class
course1.show()
course2.show()

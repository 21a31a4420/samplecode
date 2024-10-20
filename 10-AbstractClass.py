from abc import ABC , abstractmethod

class Institute:
    def __init__(self):
        print(type(self).__name__,'details:')
    def coursesOffered(self):
        print('Courses Offered: C , C++ , Java')

    @abstractmethod
    def address(self): pass

class Techno(Institute):
    def coursesOffered(self):
        print('Course Offered : Python , data science ,ML')
    def address(self):
        print('Address @ hyd')
class Online(Institute):
    def address(self):
        print('address @ HYD')

# inst=Institute()
tn=Techno()
tn.coursesOffered()
tn.address()
on = Online()
on.coursesOffered()
on.address()


class GrandParents:
    def Propland(self):
        print('Property land for farming given by grandparents')

class Parents(GrandParents):
    def PropHome(self):
        print('Property home constructed by parents' )

class Child(Parents):
    def PropVehicle(self):
        print('property car purchased by child')
    def Propland(self):
        print('Property land of GP')

c1=Child()
c1.PropVehicle()
c1.PropHome()
c1.Propland()
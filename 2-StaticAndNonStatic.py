class Test:
    staticVar=0
    instanceVar=0
    def __init__(self):
        print('Constructing the object for test class')
        self.instanceVar+=1
        Test.staticVar+=1
t1=Test()
print('After creating first object:')
print('Instance Variable:',t1.instanceVar)
print('Static Variable:',t1.staticVar)

t2=Test()
print('After creating second object:')
print('Instance Variable:',t2.instanceVar)
print('Static Variable:',t2.staticVar)
print('Static variable using class Ref. : ',Test.staticVar)






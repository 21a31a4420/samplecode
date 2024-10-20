class Father:
    def Fatherprop(self):
        print("Father's Property")
class Mother:
    def Motherprop(self):
        print('Mothers property')
class Child(Father,Mother):
    def Property(self):
        print("child will inherit:")
        super().Fatherprop()
        super().Motherprop()
c1=Child()
c1.Property()


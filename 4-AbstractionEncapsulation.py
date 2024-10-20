class Product:
    def __init__(self):
        self.__prodid=""
        self.__prodname=""   #private variables 
        self.__price=""
    def setprod(self,pid,pname,price):
        self.__prodid=pid
        self.__prodname=pname  
        self.__price=price 
    def updataprod(self,newprice):
        self.__price=newprice
    def showprod(self):
        print("ProdId: {}\n Prodname:{}\nPrice: {}".format(self.__prodid,self.__prodname,self.__price))

tv=Product()
tv.setprod('TV101','LG',18500)
# tv.__prodname='GLl'
tv.showprod()
tv.updataprod(9500)
tv.showprod()

class Employee:
    def __init__(self,empno,ename,salary,deptno):
        self.Empno=empno
        self.Ename=ename
        self.Salary=salary
        self.Deptno=deptno
    def showEmployee(self):
        print('Employee #: {}\n Employee Name:{}\n Salary : {}\nDepartment #:{}'.format(self.Empno,self.Ename,self.Salary,self.Deptno))

class Salesman(Employee):
    def __init__(self,empno,ename,salary,deptno,comm):
        self.commission=comm
        super().__init__(empno,ename,salary,deptno)
emp=Salesman(101,'Prasanthi',8500,10,500)
emp.showEmployee()
print("COmmission:",emp.commission)
class Employee:
    TotalEmployees=0
    def __init__(self,empno,ename,salary,deptno):
        self.Empno=empno
        self.Ename=ename
        self.Salary=salary
        self.Deptno=deptno
        Employee.TotalEmployees +=1
    def showEmployee(self):
        print('Employee #: {}\n Employee Name:{}\n Salary : {}\nDepartment #:{}'.format(self.Empno,self.Ename,self.Salary,self.Deptno))

emp1=Employee(101,'Prasanthi',8400,4)
emp2=Employee(102,'San',8100,5)
print('Total employees:',Employee.TotalEmployees)
emp1.showEmployee()
emp2.showEmployee()
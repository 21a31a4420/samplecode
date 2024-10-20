class Name:
    def __init__(self,firstname,midname,lastname):
        self.fn=firstname
        self.mn=midname
        self.ln=lastname
class Student:
    def __init__(self,rolno,sname,course):
        self.rn=rolno
        self.studentname=sname
        self.crs=course
std1=Student(101,Name('Pentapati','','Prasanthi'),"Object Oriented Programming with Python")
std2=Student(102,Name('Pentapati','Krishna','Lokesh'),'OOPS')
std3=Student(103,Name('Pentapati','','Arjamani'),'OOPS')
students=[std1,std2,std3]
for student in students:
    print("RollNumber:{}\nStudent Name: {} {} {}\n Course Enrolled: {}\n".format(student.rn,student.studentname.fn,student.studentname.mn,student.studentname.ln,student.crs)
    )

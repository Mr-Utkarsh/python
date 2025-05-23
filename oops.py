'''OOPS:-
1.class
2.object
3.constructor-> __init__
4.self-is a referrence variable that holds the address of the current object'''

'''class First: 
    pass
print(id(First))
obj=First
print(id(obj))
obj1=First()
print(id(obj1))'''

'''class First: 
    pass
print(dir(First))'''

'''class First: 
    "Hello pass"
# print(dir(First))
print(First.__doc__)'''

'''class First: 
    def __init__(self): 
        print("Constructor called")
        print(id(self))
# obj=First
obj=First()
print(id(obj))''' 


'''class Student: 
    def __init__(self,name,city,phone): 
        self.n=name
        self.c=city
        self.p=phone
obj=Student('Utkarsh','Bhopal',93939333993)
obj1=Student('Siddharth','Bhopal',93939333993)
obj2=Student('Raj','Bhopal',93939333993)
print(obj.n,obj.c,obj.p)
print(obj1.n,obj1.c,obj1.p)
print(obj2.n,obj2.c,obj2.p)'''

'''Variable:-
1.Instance variable(object dependent)
2.class/static variable(object independent )
3.local variable(scope or block dependent)
1.INSTANCE VARIABLE:-
declaration->1.inside class(In-side constructor)
             2.out-side class(In-side instance method)
Access->1.In-side class(In-side constructor)
        2.Out-side class(In-side instance method)'''
'''
class Student: 
    def __init__(self,name,city): 
        self.n=name   #in-side constructor
        self.c=city
        print(self.n,self.c) #access in-side constructor
    def add(self,phone): 
        self.p=phone
        print(self.n,self.c,self.school,self.p)#in-side instance method
obj=Student('Utkarsh','Bhopal')
obj.school='Ghss'     #Out-side of the class(declaration)
obj.add(9292929992292)
print(obj.n,obj.c,obj.school,obj.p) #access out-side of the class'''

'''2.class/static variable(object independent):-
declaration->1.inside class body
             2.in-side constructor
             3.in-side instance method
             4.in-side class method
             5.out-side of the class
Access->1.In-side constructor
        2.In-side instance method
        3.in-side class method(modification)
        4.out-side of the class'''

'''class Student: 
    school='SHSS' #declaration inside class body
    def __init__(self,name): 
        self.n=name
obj1=Student('Utkarsh')
obj2=Student('Siddharth')
# print(obj1.School)
# print(obj2.School)
print(Student.school)'''

'''class Student: 
    school='SHSS' #declaration inside class body
    def __init__(self,name): 
        self.n=name
        Student.school_code=101 ##declaration inside constructor
        print(Student.school)
    def addnew(self):
        Student.school_city='Bhopal' ##declaration inside instance method
        print(Student.school,Student.school_code,Student.school_city)
    def display(self):
        print(Student.grade)
Student.grade='10th' ##declaration outside of the class
obj=Student('Utkarsh')
obj.addnew()
obj.display()
print(Student.school,Student.grade,Student.school_code,Student.school_city)'''

'''3.local variable:-

class Student:
    def __init__(self,name):
        grade='10th'
        self.name=name
        print(grade)
    def new(self): 
        print(grade)
obj=Student('Utkarsh')
obj.new()'''


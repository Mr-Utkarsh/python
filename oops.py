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


'''Methods:-
1.Instance
2.class
3.static

2.class method'''
'''class Student: 
    school='Ghss'
    grade='10th'
    def __init__(self,name): 
        self.n=name
    def show_details(self): 
        print(self.n)
        print(Student.school)
        print(Student.grade)
    @classmethod
    def update_grade(cls,updated): 
        cls.grade=updated
obj=Student('Utkarsh')
obj.show_details()
Student.update_grade('11th')
obj2=Student('Siddharth')
obj2.show_details()'''

'''class Student: 
    school='Ghss'
    grade='10th'
    def __init__(self,name): 
        self.n=name
    def show_details(self): 
        print(self.n)
        print(Student.school)
        print(Student.grade)
        print(Student.city)
    @classmethod
    def update_grade(cls,updated): 
        cls.grade=updated
    @classmethod
    def add_new(cls,city): 
        cls.city=city
obj=Student('Utkarsh')
# obj.show_details()
Student.update_grade('11th')
obj2=Student('Siddharth')
# obj2.show_details()
Student.add_new('Bhopal')
obj2.show_details()
'''

'''3.static method

class Student: 
    school='Ghss'
    grade='10th'
    def __init__(self,name): 
        self.n=name
    def show_details(self): 
        print(self.n)
        print(Student.school)
        print(Student.grade)
    @staticmethod
    def add_new(self,cls,city): 
        print(self)
        print(cls)
        print(city)
    @staticmethod
    def welcome(): 
        print('welcome')
    @staticmethod
    def thanks(): 
        print('thanks')
Student.welcome()
obj=Student('Utkarsh')
obj2=Student('Siddharth')
Student.add_new('Bhopal','Indore','Jabalpur')
obj2.show_details()
Student.thanks()'''


'''OOPS PROPERTIES

1.Abstraction
2.Inheritance
3.polymorphism
4.encapsulation'''

'''INHERITANCE

1.SINGLE LEVEL'''

'''class Parent: 
    x=10
    def __init__(self,name): 
        self.name=name
    def home(self): 
        print("home from parent class")
class Child(Parent): 
    pass
obj=Child()'''

'''class Parent: 
    x=10
    def __init__(self,name): 
        self.name=name
    def home(self): 
        print("home from parent class")
class Child(Parent): 
    pass
obj=Child('Python')
print(obj.x)
print(obj.name)
obj.home()'''

'''class Parent: 
    x=10
    def __init__(self,name): 
        self.name=name
    def home(self): 
        print("home from parent class")
class Child(Parent): 
    def home(self): 
        print("home from child class")
        super().home()
obj=Child('Python')
print(obj.x)
print(obj.name)
obj.home()'''

'''2.Multi level

class GParent: 
    def car(self): 
        print("car from GParent class")
class Parent(GParent): 
    x=10
    def __init__(self,name): 
        self.name=name
    def home(self): 
        print("home from parent class")
class Child(Parent): 
    def home(self): 
        print("home from child class")
        super().home()
obj=Child('Python')
print(obj.x)
print(obj.name)
obj.home()
obj.car()'''

'''class Parent1: 
    def car(self): 
        print("car from Parent1 class")
class Parent2: 
    x=10
    def __init__(self,name): 
        self.name=name
    def home(self): 
        print("home from Parent2 class")
class Child(Parent1,Parent2): 
    def home(self): 
        print("home from child class")
        super().home()
obj=Child('Python')
print(obj.x)
print(obj.name)
obj.home()
obj.car()'''

'''class Parent: 
    x=10
    def __init__(self,name): 
        self.name=name
    def home(self): 
        print("home from Parent2 class")
class Child1(Parent): 
    def home(self): 
        print("home from child class")
        super().home()
class Child2(Parent): 
    pass
obj1=Child1('Python')
obj2=Child2('Java')
obj.home()
print(obj1.name,obj2.name)'''

'''3.Hybrid level
Method Resolution Order:-

class A: 
    def first(self): 
        print("from class A")
class B: 
    def first(self): 
        print("from class B")
class C(A): 
    pass
class D(B): 
    pass
class E(C,D): 
    pass
class C(A): 
    pass
obj=E()
obj.first()'''

'''class A: 
    def first(self): 
        print("from class A")
class B: 
    def first(self): 
        print("from class B")
class C(A): 
    pass
class D(B): 
    pass
class E(D,C): 
    pass
class C(A): 
    pass
obj=E()
obj.first()'''

# ABSTRACTIION

'''from abc import ABC,abstractmethod
class Senior(ABC): 
    def add(self,x,y): 
        print(x+y)
    def sub(self,x,y): 
        print(x-y)
    def multi(self,x,y): 
        print(x*y)
    @abstractmethod
    def div(self,x,y): 
        pass
class Junior(Senior): 
    def div1(self,x,y): 
        print(x/y)
obj=Junior()'''

'''from abc import ABC,abstractmethod
class Senior(ABC): 
    def add(self,x,y): 
        print(x+y)
    def sub(self,x,y): 
        print(x-y)
    def multi(self,x,y): 
        print(x*y)
    @abstractmethod
    def div(self,x,y): 
        pass
class Junior(Senior): 
    def div(self,x,y): 
        print(x/y)
obj=Junior()
obj.add(2,3)
obj.sub(6,3)
obj.multi(2,3)
obj.div(4,2)'''

# Encapsulation

'''class P: 
    x=10
    def show(self): 
        print("from p class")
class C(P): 
    pass
obj=C()
print(obj.x)
print(obj.show())'''

'''class P: 
    _x=10
    def _show(self): 
        print("from p class")
class C(P): 
    pass
obj=C()
print(obj._x)
print(obj._show())'''

'''class P: 
    __x=10
    def __show(self): 
        print("from p class")
class C(P): 
    pass
obj=C()
print(obj.__x)
print(obj.__show())'''

'''class P: 
    __x=10
    def __show(self): 
        print("from p class")
class C(P): 
    print(P.__x)
obj=C()
# print(obj.__x)
# print(obj.__show())'''

'''class P: 
    __x=10
    def __show(self): 
        print("from p class")
class C(P): 
    pass
print(dir(C))'''

'''class P: 
    __x=10
    def __show(self): 
        print("from p class")
class C(P): 
    pass
print(dir(C))
obj=C()
print(obj._P__show())'''

'''class P: 
    __x=10
    def __show(self): 
        print("from p class")
class C(P): 
    pass
print(dir(C))
obj=C()
obj._P__show()'''
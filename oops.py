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
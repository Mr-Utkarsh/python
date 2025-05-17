# Function:-
# 1.Inbuilt Function
# 2.user-define functionDeclaration Syntax:-
# def fun-name(parameter):
#     used variables are declared as parameter
#     =>perform operation
#     =>return
# function calling
# fun-name(arguments(args are values against declare parameter))


# required:-
# =>def(keyword)
# =>fun-name
# =>()
# =>:
# =>body

# optional:-
# =>parameter
# =>arguments
# =>return(keyword)



# def hello():
#     pass
# hello()
# print(hello())

# def hello():
#     return None
# hello()
# print(hello())

# def hello():
#     return 'hello'
# hello()
# print(hello())

# def hello():
#     return
# hello()
# print(hello())

# def hello():
#     return ''
# hello()
# print(hello())

# def hello():
#     print("hello")
# hello()

# def hello():
#     print("hello")
# x=hello()
# print(x)
# print(x)
# print(x)

# def hello():
#     return "hello"
# x=hello()
# print(x)
# print(x)
# print(x)

# def natural_no(n): 
#     for i in range(1,n+1): 
#         print(i)
# x=int(input("Enter any value = "))
# natural_no(x)

# def natural_no(n): 
#     for i in range(1,n+1): 
#         if i%2==0: 
#             print(i)
# x=int(input("Enter any value = "))
# natural_no(x)

# def natural_no(n): 
#     for i in range(1,n+1): 
#         if i%2!=0: 
#             print(i)
# x=int(input("Enter any value = "))
# natural_no(x)

# def natural_no(n): 
#     sum=0
#     for i in range(1,n+1): 
#         if i%2!=0: 
#             sum+=i
#     print(sum)
# x=int(input("Enter any value = "))
# natural_no(x)

# def natural_no(n): 
#     sum=0
#     for i in range(1,n+1): 
#         if i%2==0: 
#             sum+=i
#     print(sum)
# x=int(input("Enter any value = "))
# natural_no(x)

# def factorial(n): 
#     fact=1
#     for i in range(1,n+1): 
#         if i>0: 
#             fact*=i
#     print(fact)
# x=int(input("Enter any value = "))
# factorial(x)

# def find_factors(number):
#     print(f"Factors of {number} are:")
#     for i in range(1, number + 1):
#         if number % i == 0:
#             print(i)

# # Example usage:
# num = int(input("Enter a number: "))
# find_factors(num)

# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a leap year.")
#     else:
#         print(f"{year} is not a leap year.")
# yr = int(input("Enter a year: "))
# is_leap_year(yr)

# def fibonacci(number): 
#     a=0
#     b=1
#     for i in range(1,number+1): 
#         c=a+b
#         if i<number: 
#             print(a,end=",")
#             a,b=b,c
#         else: 
#             print(a)
# num=int(input("Enter a number = "))
# fibonacci(num)




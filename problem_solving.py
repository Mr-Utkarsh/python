# Loops in python
# 1. counting positive numbers
# problem: Give a list of numbers,count how many are positive

'''numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
positive_numbers_count=0
for num in numbers:
    if num>0:
        positive_numbers_count+=1
print("final count of positive numbers is = ", positive_numbers_count)'''


# 2. counting negative numbers
# problem: Give a list of numbers,count how many are positive
'''numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
negative_numbers_count=0
for num in numbers:
    if num<0:
        negative_numbers_count+=1
print("final count of negative numbers is = ", negative_numbers_count)'''

# 3.calcuate the sum of even numbers upto n
'''n=int(input("Enter any no = "))
sum=0
for i in range(2,n+1): 
    if i%2==0: 
        sum+=i
print(sum)'''

#4.multiplication table printer
# problem: print the multiplactiontable for a given number upto 10,but skip the fifth iteration
'''number=int(input("enter the number to print the table of = "))
for i in range(1,11):
    if i==5:
        continue
    print(number,'x',i,'=',number*i)'''

#5.reverse a string using loop
'''string=str(input("enter any string = "))
rev=""
for char in string:
    rev=char+rev
print(rev)'''

#6.find the first non-repeated character
#problem: givebn a string,find the first non-repeated character
'''string = "teeteracdacd"
for char in string:
    print(char)
    if string.count(char)==1:
        print("char is = ",char)
        break'''

#7.Compute the factorial of a number using while loop
'''number=int(input("Enter a number = "))
factorial=1
while number>0:
    factorial*=number
    number-=1
print(factorial)'''

#8.validate input
#problem:keep asking the user for input until they enter a number between 1 and 10.
'''while True:
    number=int(input("enter a value btw 1 and 10 = "))
    if 1<=number<=10:
        print("thanks")
        break
    else:
        print("Invalid number,try again")
'''

#9.prime number
'''number = 1
is_prime=True
if number>1:
    for i in range(2,number):
        if(number%i==0):
            is_prime=False
            break
print(is_prime)'''

#10.List unique checker
#problem: Check if all elements in a list are unique.if a dulicate is found,exit the loop and print the duplicate.
'''items=['apple','banana','orange','apple','mango']
unique_item = set()
for item in items:
    if item in unique_item:
        print("Duplicate item",item)
        break
    unique_item.add(item)'''


#Restaurant menu
'''print("Welcome to Pythonic Restaurant!")
print("Here is our menu:")
print("1. Burger - ₹80")
print("2. Pizza - ₹150")
print("3. Sandwich - ₹50")
print("4. Coffee - ₹40")
print("5. Exit")

total = 0

while True:
    choice = input("\nEnter the item number you want to order (1-5): ")

    if choice == '1':
        total += 80
        print("Burger added to your order. Total =", total)
    elif choice == '2':
        total += 150
        print("Pizza added to your order. Total =", total)
    elif choice == '3':
        total += 50
        print("Sandwich added to your order. Total =", total)
    elif choice == '4':
        total += 40
        print("Coffee added to your order. Total =", total)
    elif choice == '5':
        print("\nThank you for ordering!")
        print("Your final bill is ₹", total)
        break
    else:
        print("Invalid choice. Please select a valid item number.")

'''

'''n=int(input("Enter the number of rows: "))
for i in range(0,n+1):
print(" "*(n-i),"*"*i)
for i in range(n,0,
-1):
print("*"*i,
" "*(n-i))
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *'''

# l=[1,2,3,4,5]
# def add5(n): 
#     return n+5
# x=map(add5,l)
# print(x)
# print(tuple(x))

# l1=[1,2,3,4,5]
# l2=[5,4,3,2,1]
# def add5(n,m): 
#     return n+m
# x=map(add5,l1,l2)
# print(x)
# print(tuple(x))

# l1=[1,2,3,4,5]
# l2=[5,4,3,2,1]
# def add5(n,m): 
#     return n**m
# x=map(add5,l1,l2)
# print(x)
# print(tuple(x))

# l1=[1,2,3,4,5]
# l2=[5,4,3,2,1]
# def add5(n,m): 
#     return n//m
# x=map(add5,l1,l2)
# print(x)
# print(tuple(x))

# l1=[1,2,3,4,5]
# l2=[5,4,3,2,1]
# def add5(n,m): 
#     return n-m
# x=map(add5,l1,l2)
# print(x)
# print(tuple(x))

#star pattern using while loop 

# 1.  *****
#     *****
#     *****
#     *****
#     *****
# n=int(input("Enter any value="))
# i=1
# while i<=n: 
#     print('*'*n)
#     i=i+1

#2.*
#  **
#  ***
#  ****
#  *****
# n=int(input("Enter any value="))
# i=1
# while i<=n: 
#     print('*'*i)
#     i=i+1

#3.   *
#    **
#   ***
#  ****
# *****
# n=int(input("Enter any value="))
# i=1
# while i<=n: 
#     print(" "*(n-i)+"*"*i)
#     i=i+1

#4.    *
#     * *
#    * * *
#   * * * *
#  * * * * *
# n=int(input("Enter any value="))
# i=1
# while i<=n: 
#     print(" "*(n-i)+" *"*i)
#     i=i+1

#5.*****
#  *****
#   ****
#    ***
#     **
#      *
# n=int(input("Enter any value="))
# i=0
# while i<n: 
#     print(" "*i+"*"*(n-i))
#     i=i+1

#6. * * * * *
#    * * * *
#     * * *
#      * *
#       *
# n=int(input("Enter any value="))
# i=0
# while i<n: 
#     print(" "*i+" *"*(n-i))
#     i=i+1

#7.*****
#  ****
#  ***
#  **
#  *
# n=int(input("Enter any value="))
# while n>0: 
#     print("*"*n)
#     n=n-1

#8.
# *****
# **** 
# ***  
# **   
# *    
# **   
# ***  
# **** 
# *****
# n=int(input("Enter any value="))
# i=0
# while i<n: 
#     print("*"*(n-i)+" "*i)
#     i=i+1
# # print(i)
# i=i-2
# while i>=0: 
#     print("*"*(n-i)+" "*i)
#     i=i-1

#9.
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# n=int(input("Enter any value="))
# i=0
# while i<n: 
#     print(" "*i+" *"*(n-i))
#     i=i+1
# # print(i)
# i=i-2
# while i>=0: 
#     print(" "*i+" *"*(n-i))
#     i=i-1

#10.
#     *
#    **
#   ***
#  ****
#   ***
#    **
#     *
# n=int(input("Enter any value="))
# i=0
# while i<n: 
#     print(" "*(n-i)+"*"*i)
#     i=i+1
# # print(i)
# i=i-2
# while i>=0: 
#     print(" "*(n-i)+"*"*i)
#     i=i-1

#11.
#      *
#     * *
#    * * *
#   * * * *
#    * * *
#     * *
#      *
# n=int(input("Enter any value="))
# i=0
# while i<n: 
#     print(" "*(n-i)+" *"*i)
#     i=i+1
# # print(i)
# i=i-2
# while i>=0: 
#     print(" "*(n-i)+" *"*i)
#     i=i-1

#12.
# *****
#  ****
#   ***
#    **
#     *
#    **
#   ***
#  ****
# *****
# n=int(input("Enter any value="))
# i=0
# while i<n: 
#     print(" "*i+"*"*(n-i))
#     i=i+1
# # print(i)
# i=i-2
# while i>=0: 
#     print(" "*i+"*"*(n-i))
#     i=i-1 

# perfect number
'''n=int(input("Enter any no:"))
sum = 0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if n==sum:
    print(f'given number {n} is a perfect number')
else:
    print(f'given number {n} is not a perfect number')'''

# WAP to arrenge all zeroes at the end.
'''l = [2,0,3,0,1,0,5] # [2,3,1,5,0,0,0]
l1=[]
for i in l:
    if i !=0:
        l1.append(i)
    n = len(l)-len(l1)
for i in range(n):
    l1.append(0)
print(l1)'''


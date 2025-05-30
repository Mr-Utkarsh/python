'''# Factors :---
n=int(input("Enter any no:"))
factors = []
for i in range(1,n+1):
if n%i==0:
factors.append(i)
print("Factors are :",factors)
# WAP to arrenge all items from list in assending order.
l = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(l)
for i in range(n-1):
for j in range(n-i-1):
if l[j] > l[j+1]:
l[j], l[j+1] = l[j+1], l[j]
print(l)
# WAP to arrenge all items from list in desending order.
l = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(l)
for i in range(n-1):
for j in range(n-i-1):
if l[j] < l[j+1]:
l[j], l[j+1] = l[j+1], l[j]
print(l)
# WAP to find maximum digit in given list.
l = [2,4,9,3,5]
max = l[0]
for i in range(len(l)-1):
if l[i]>l[i+1]:
max = l[i]
l[i],l[i+1]=l[i+1],l[i]
else:
max=l[i+1]
print(max)
# WAP to find minimum digit in given list.
l = [2,4,9,3,5]
min = l[0]
for i in range(len(l)-1):
if l[i]<l[i+1]:
min = l[i]
l[i],l[i+1]=l[i+1],l[i]
else:
min=l[i+1]
print(min)
# Perfect number...
n=int(input("Enter any no:"))
sum = 0
for i in range(1,n):
if n%i==0:
sum=sum+i
if n==sum:
print(f'given number {n} is perfect number')
else:
print(f'given number {n} is not a perfect number')
# WAP to arrenge all even and odd no at a place.
l = [2,1,3,8,4,8,5] # [2,8,4,8,1,3,5]
l1=[]
for i in l:
if i %2==0:
l1.append(i)
for i in l:
if i%2 !=0:
l1.append(i)
print(l1)
# WAP to arrenge all zeroes at the end.
l = [2,0,3,0,1,0,5] # [2,3,1,5,0,0,0]
l1=[]
for i in l:
if i !=0:
l1.append(i)
n = len(l)-len(l1)
for i in range(n):
l1.append(0)
print(l1)
----: Some Important Pattern examples :---
c n=5 Clo1 Clo2 Clo3 Clo4 Clo5 Formulla
1 Row1 1 range(1,2) range(1, 1+1) 2 Row2 1 2 range(1,3) range(1, 2+1) 3 Row3 1 2 3 range(1,4) range(1, 3+1) 4 Row4 1 2 3 4 range(1,5) range(1, 4+1) 5 Row5 1 2 3 4 5 range(1,6) range(1, 5+1) i n=5 Clo1 Clo2 Clo3 Clo4 Clo5 Formulla
1 Row1 1 2 3 4 5 range(1,6) range(1, 5+1) 2 Row2 1 2 3 4 5 range(1,6) range(1, 5+1) 3 Row3 1 2 3 4 5 range(1,6) range(1, 5+1) 4 Row4 1 2 3 4 5 range(1,6) range(1, 5+1) 5 Row5 1 2 3 4 5 range(1,6) range(1, 5+1) # 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
n = int(input("Enter any no :"))
for i in range(1,n+1):
for j in range(1,n+1):
print(j,end=' ')
print()
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
n = int(input("Enter any no :"))
for i in range(1,n+1):
for j in range(1,i+1):
print(j,end=' ')
print()
range(1, i+1)
range(1, i+1)
range(1, i+1)
range(1, i+1)
range(1, i+1)
range(1, n+1)
range(1, n+1)
range(1, n+1)
range(1, n+1)
range(1, n+1)
# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E
n = int(input("Enter any no :"))
for i in range(1,n+1):
ch='A'
for j in range(1,n+1):
print(ch,end=' ')
ch=chr(ord(ch)+1)
print()
# A
# A B
# A B C
# A B C D
# A B C D E
n = int(input("Enter any no :"))
for i in range(1,n+1):
ch = 'A'
for j in range(1,i+1):
print(ch,end=' ')
ch=chr(ord(ch)+1)
print()
# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10
n = int(input("Enter any no :"))
for i in range(1,n+1):
for j in range(1,i+1):
print(2*j,end=" ")
print()
# 1
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9
# code for above output
n = int(input("Enter any no :"))
for i in range(1,n+1):
for j in range(1,i+1):
print(2*j-1,end=" ")
print()
# O/P:--
# 10
# 10 8
# 10 8 6
# 10 8 6 4
# 10 8 6 4 2
# code for above output
k=[]
for i in range(10,1,
-2):
k.append(i)
for j in k:
print(j,end=" ")
print()
# O/P:-- {1: 2, 2: 3}
# code for above output
t=(1,1,2,2,4,2)
dict={}
for i in t:
count=0
for j in t:
if j==i:
count=count+1
if count>=2:
dict[i]=count
print(dict)
# O/P --- {1: 2, 2: 3, 4: 1}
# code for above output
t=(1,1,2,2,4,2)
dict={}
for i in t:
count=0
for j in t:
if j==i:
count=count+1
dict[i]=count
print(dict)
# *
# **
# ***
# ****
# *****
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
print("*"*i)
# *
# * *
# * * *
# * * * *
# * * * * *
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
print("* "*i)
# *
# **
# ***
# ****
# *****
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
print(" "*(n-i),"*"*i)
# *
# ***
# *****
# *******
# *********
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
print(" "*(n-i),"*"*(2*i-1))
# *
# * *
# * * *
# * * * *
# * * * * *
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
print(" "*(n-i)," *"*i)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
for j in range(1,i+1):
print(j,end=" ")
print()
# *****
# ****
# ***
# **
# *
n=int(input("Enter the number of rows: "))
for i in range(n,0,
-1):
print(" "*(n-i),"*"*i)
# *****
# ****
# ***
# **
# *
n=int(input("Enter the number of rows: "))
for i in range(n,0,
-1):
print("*"*i)
# * * * * *
# * * * *
# * * *
# * *
# *
n=int(input("Enter the number of rows: "))
for i in range(n,0,
-1):
print(" "*(n-i)," *"*i)
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
print(" "*(n-i),"* "*i)
m=n-1
for i in range(m,0,
-1):
print(" "*(m-i)," *"*i)
# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *
n=int(input("Enter the number of rows: "))
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
# *
n=int(input("Enter the number of rows: "))
for i in range(0,n+1):
print("* "*i)
m=n-1
for i in range(m,0,
-1):
print("* "*i)
# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *
n=int(input("Enter the number of rows: "))
for i in range(0,n+1):
print(" "*(n-i),"*"*i)
for i in range(n,0,
-1):
print(" "*(n-i),"*"*i)
IF-ELIF-ELSE STATEMENT EXAMPLES
Example 1: Write a program to check given no is positive. (Only if-statement)
Example 2: Write a program to check given no is positive or negative. (Only if-else
statement)
Example 3: Write a program to check given no is positive, negative or Zero.(Only if-
elif-else statement)
Example 4: Write a program to swap two variables without using third variable.
Example 5: Write a program to swap two variables using third variable.
Example 6: Write a program to swap two variables using using Addition and
Subtraction.
Example 9: Write a program to find squre root of given no.
Example 10: Write a program to find largest no among the three inputs numbers.
Example 11: Write a program to find area of triangle. (1/2* hight*base)
Example 12: Write a program to find area of square.
Example 13: Write a program to find given year is leep year or not.
While-Loop EXAMPLES
Example 1: Write a program to display n natural numbers. (In Horizontal-
1,2,3,4,5…….. )
Example 2: Write a program to calculate the sum of numbers.
Example 3: Write a program to find even no. (2,4,6,8,….)
Example 4: Write a program find odd no.(1,3,5,7,9,……)
Example 5: Write a program to find factorial of given no.
Example 6: Write a program to print your names ten times.
Example 7: Write a program to find how many vowels and consonants are present
in strings.
Example 8: Write a program to add 5 in each elements in given list.
[10,20,30,40,50]
Example 9: Write a program to add 5 in each elements in given tuple.
(10,20,30,40,50)
Example 10: Write a program to create a list from given string.
Examples for FOR_LOOPs
Example 1: Print the first 10 natural numbers using for loop.
Example 2: Python program to print all the even numbers within the given range.
Example 3: Python program to calculate the sum of all numbers from 1 to a given number.
Example 4: Python program to calculate the sum of all the odd numbers within the given range.
Example 5: Python program to print a multiplication table of a given number
Example 6: Python program to display numbers from a list using a for loop.
Example 7: Python program to count the total number of digits in a number.
Example 8: .(madam=madam)
Example 9: Python program that accepts a word from the user and reverses it.
Example 10: Python program to check if a given number is an Armstrong number.
(153=1**3+5**3+3**3)
Example 11: Python program to count the number of even and odd numbers from a series of
numbers.
Example 12: Python program to display all numbers within a range except the prime numbers.
Example 13: Python program to get the Fibonacci series. (0,1,1,2,3,5,8,13,21……………..)
Example 14: Python program to find the factorial of a given number.
Example 15: Python program that accepts a string and calculates the number of digits and letters.
Example 16: Write a Python program that iterates the integers from 1 to 25.
Example 17: Python program to check the validity of password input by users.
Example 18: Python program to convert the month name to a number of days.'''
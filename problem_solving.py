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


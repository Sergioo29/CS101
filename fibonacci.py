# 1. Name:
# Sergio Henrique
# 2. Assignment Name:
# Lab 10: Fibonacci
# 3. Assignment Description:
# This program will prompt the user for a positive integer n and then display
#the nth Fibonacci number.
# 4. What was the hardest part? Be as specific as possible.
# With the pseudocode, my job here was actually pretty easy. Not that I'm
#complaining, though... haha!
# The hardest part was defining the asserts. The assert syntax is something
#brand new for me, but I liked them.
# I also had to word with the pseudocode part A, so I can have a function call
#and return.
# 5. How long did it take for you to complete the assignment?
# 6h
def fibonacci(num):
if num == 1 or num == 2:
fibon = 1 #B
else:
first = 1
second = 1
index = 3 #The index (from 1) where the fibonacci starts to change #C
while index <= num:
fibon = first + second # A swap
first = second
second = fibon #D
index+=1
#Paranoia
assert type(fibon) == int and fibon > 0, "Your fibonacci is of the standards"
return fibon
#---------------------------------------------------------------------------------
#The input itself assert that the given number is a integer
number = int(input("\nWhich Fibonacci number would you like to see? ")) #A
# I could do just "num > 0", but I split it in order to have a specific message
assert number != 0, "\nThe number can't be zero!\n"
assert number > 0, "\nThe number can't be negative!\n"
fibon = fibonacci(number)
print ("\nFibonacci number %s is: %s" % (number, fibon))

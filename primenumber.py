# 1. Name:
# Sergio Henrique
# 2. Assignment Name:
# Lab 12: Prime Numbers
# 3. Assignment Description:
# This program will display all the prime numbers at or below a certain
#value.
# It will first prompt the user for an integer. If the integer is less than 2,
#then
# the program will prompt the user for another number. The program will then
#compute
# all the prime numbers below (and including) the given number. When finished,
#the
# program will display the list of prime numbers.
# 4. What was the hardest part? Be as specific as possible.
# The math here was quite hard to understand. I have watched the Video
#Solution and
# still didn't get much about the math (I get the overall concept, though).
#But, I
# tried to follow strictly the given Pseudocode, and it works, so...
# I had my own solution, but it has a significantly different syntax.
# 5. How long did it take for you to complete the assignment?
# 11h
import math # For the square root
print ("\nThis program will find all the prime numbers at or below N.")
num = int(input("Select that N: "))
assert num > 1, "The N has to be greather than 1"
numbers = []
for fill_true in range(num+1):
numbers.append(True)
numbers[0] = False
numbers[1] = False
#----------------------------------------------
for factor in range (2, (int(math.sqrt(num))+1)):
if numbers[factor]:
multiple = factor * 2
for multiple in range(multiple, (num+1), factor):
numbers[multiple] = False
primes = []
for index in range(2, (num+1)):
if numbers[index]:
primes.append(index)
exit("\nThe prime numbers at or below %s are %s" % (num, primes))

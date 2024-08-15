# 1. Name:
# Sergio Henrique
# 2. Assignment Name:
# Lab 01: Guessing Game
# 3. Assignment Description:
# With the "random library", we ask the user for a number cap, then we use
#"random" to
# pick a number from 1 to the cap (limit) and the user has unlimited chances
#to find out the nº
# all the attempts will be stored in a "list" to be shown later.
# 4. What was the hardest part? Be as specific as possible.
# First, I have to mention that I already have a similar code on CS 101, I
#just have to addapt to this
# assigment cause it was slightly different: I had to add the cap (the other
#had a static cap of 1-100);
# I had to create a list to store the attempt values (the CS101 just had the
#number os times). I forgot
# how to add values to a list without replacing the existing values, so I had
#to look through my
# Codecademy assignments to remember the "append" function. I just learned the
#first version of Python,
# so I also had to learn how the print works on Phyton 3 (how to add variables
#within the text...)
# 5. How long did it take for you to complete the assignment?
# 6h
import random
print ("This is the \"guess a number\" game.")
print ("You try to guess a random number in the smallest number of attempts.")
print ("")
limit = int(input("Pick a positive integer: "))
n = random.randint(1, limit)
guess = 0
count = 0
fail = []
print ("Guess a number between 1 and %i." % (limit))
#----------------------------------------------------------------------------
while guess != n:
count += 1
guess = int(input("> "))
if guess == n:
fail.append(guess)
print ("You were able to find the number in %i guesses." % (count))
print ("The numbers you guessed were %s." % (fail))
else:
if guess < n:
print ("\tToo LOW !")
fail.append(guess)
if guess > n:
print ("\tToo HIGH !")
fail.append(guess)
#----------------------------------------------------------------------------

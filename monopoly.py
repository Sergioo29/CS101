# Sergio Henrique
# 2. Assignment Name:
# Lab 04: Monopoly
# 3. Assignment Description:
# This program will give the instructions to help a Monopoly player ")
# to build a hotel on Pennsylvania Avenue, based on the given info.
# 4. What was the hardest part? Be as specific as possible.
# It was laborous but not hard.
# I like to create if statements and print messages
# 5. How long did it take for you to complete the assignment?
# 8h
print ("\tThis program will give the instructions to help a Monopoly player ")
print ("\tto build a hotel on Pennsylvania Avenue, based on the given info.\n")
# PLAYER INPUT
#----------------------------------------------------------------------------------
------------
own_all = str(input("Do you own all the green properties? (y/n) "))
if own_all == "n" or own_all == "N":
exit("You cannot purchase a hotel until you own all the properties of a given
color group.")
elif own_all == "y" or own_all == "Y":
own_all = "ok"
else:
print ("Did you mean yes? I will assume so, moving on...\n")
player_cash = int(input("How much cash do you have to spend? "))
if player_cash < 400:
exit("You do not have sufficient funds to purchase a hotel at this time.")
available_houses = int(input("How many houses are there to purchase? "))
if available_houses <= 0:
exit("There are not enough houses available for purchase at this time.")
available_hotels = int(input("How many hotels are there to purchase? "))
if available_hotels <= 0:
exit("There are not enough hotels available for purchase at this time.")
penn_ave = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ...
5:a hotel) "))
if penn_ave >= 5:
exit ("You cannot purchase a hotel if the property already has one.")
elif penn_ave < 0:
exit ("You cannot have a negative property")
# if there is a hotel, swap it and exit
nc_ave = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ...
5:a hotel) "))
if nc_ave >= 5:
temp_value = penn_ave
penn_ave = nc_ave
nc_ave = temp_value
exit("Swapped the hotel from North Carolina to Pennsylvania")
elif nc_ave < 0:
exit ("You cannot have a negative property")
# if there is a hotel, swap it and exit
pac_ave = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a
hotel) "))
if pac_ave >= 5:
temp_value = penn_ave
penn_ave = pac_ave
pac_ave = temp_value
exit("Swapped the hotel from Pacific to Pennsylvania")
elif pac_ave < 0:
exit ("You cannot have a negative property")
print ("\n")
#----------------------------------------------------------------------------------
---------------
FOUR_HOUSE_RANK = 4
penn_ave_needs = FOUR_HOUSE_RANK - penn_ave
nc_ave_needs = FOUR_HOUSE_RANK - nc_ave
pac_ave_needs = FOUR_HOUSE_RANK - pac_ave
total_house_needs = penn_ave_needs + nc_ave_needs + pac_ave_needs
total_hotel_needs = 1 #Pennsylvania
#Determine if you can put a hotel in Penn
if total_house_needs == 0:
print ("Instructions:")
print ("-----------------------------------")
print ("You can put a hotel in Pennsylvania Avenue!")
player_cash -= 400
print ("Your remaining cash will be: $%.2f ($200.00 hotel + $200.00 bank fee)\
n" % player_cash)
total_hotel_needs = 0
available_hotels -= 1
#Determine if you can build 1 or 2 more hotels, based on cash leftover
how_many_more_possible = 0
if total_hotel_needs == 0 and player_cash >= 200:
how_many_more_possible += 1
if total_hotel_needs == 0 and player_cash >= 400:
how_many_more_possible += 1
total_hotel_needs += how_many_more_possible
hotel_cost = 200 * how_many_more_possible
if how_many_more_possible >=1:
print("You can build %s more hotels for North Carolina and/or Pacific Av."
% how_many_more_possible)
print ("-----------------------------------")
print ("This will cost $%.2f" % hotel_cost)
if available_hotels < how_many_more_possible:
print ("\tBut the bank currently has %s hotels available..." %
available_hotels)
print ("\tMake sure to save $200.00 for a possible auction.")
exit()
else:
exit()
cost = 200 * total_house_needs
#Tell player the recommendation
print ("Instructions:")
print ("--------------------------------")
if nc_ave_needs >= 1:
print ("Add %s house(s) to North Carolina," % nc_ave_needs)
if pac_ave_needs >= 1:
print ("add %s house(s) to Pacific," % pac_ave_needs)
if penn_ave_needs >= 1:
print ("add %s house(s) to Pennsylvania," % penn_ave_needs)
print ("and put 1 hotel on Pennsylvania.")
print ("--------------------------------")
if player_cash < cost:
print ("This will cost $%.2f, but you currently have $%.2f" % (cost,
player_cash))
print ("You will have to earn more $%.2f" % (cost - player_cash))
if available_houses < total_house_needs:
print ("\tYou need %s houses, the bank currently has %s available." %
(total_house_needs, available_houses))
print ("\tMake sure to save $200.00 for a possible auction.")
exit()
else:
print ("Your current cash: $%.2f" % player_cash)
print ("This will cost $%.2f" % cost)
if available_houses < total_house_needs:
print ("\tYou need %s houses, but the bank currently has %s available." %
(total_house_needs, available_houses))
print ("\tMake sure to save $200.00 for a possible auction.")
exit()if pac_ave_needs >= 1:
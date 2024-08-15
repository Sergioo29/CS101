# 1. Name:
# Sergio Henrique
# 2. Assignment Name:
# Lab 06: Advanced Search
# 3. Assignment Description:
# The user inputs a .json file and a name to search in it. Then, the program
#uses the advanced search
# to find if the name is present there, using fewer attempts possible.
# 4. Algorithmic Efficiency
# O(n log n):
# Exp: empty.json - trivial.json - languages.son (less than 12 objets)
# The number of attempts were basically the same (4 or less)
# countries.json (nearly 200 objects)
# The number of attempts doubled: 8
# 5. What was the hardest part? Be as specific as possible.
# With the pseudocode of the advanced search, my life was a lot easier here
#haha.
# I learned how to read json files on Week 2, so this wasn't a problem this
#time.
# When we have the "big picture" of the code, the details are quite easy to
#add (add a variable, a print, an if)
# Although, I had difficult with a syntax error in the advanced_search. I
#figured out that I had to add
# 'array' before the file indexes, and also the lenght and the code lines that
#I added comments.
# 6. How long did it take for you to complete the assignment?
# 9h
import json
def advanced_search(file, element):
# The word "array" used in this function is the first element name that is
certain to be the first file's index
# If this is not the case, we would have to use another syntax, like the index
number, for example.
attempts = 0
first = 0
last = int(len(file['array']) - 1) # Minus one because it starts counting at
zero
while first <= last:
middle = int((first + last) / 2) # Use INT, or else this expression will
result in a bug, same as above
if file['array'][middle] == element:
attempts +=1
print ("Attempts: %s" % attempts)
return True
if file['array'][middle] < element:
attempts +=1
first = middle + 1
else:
attempts +=1
last = middle - 1
if attempts <= 0:
print ("ERROR: No names in this file")
exit()
print ("Attempts: %s" % attempts)
return False
#----------------------------------------------------
# In this case, the user don't have to type the file type, if so, the program will
not find the file
file_name = input("\nWhat is the name of the file? ")
try:
with open("%s.json" % file_name) as JasonVoorhees: # Added the file type
data = json.load(JasonVoorhees)
except:
print ("\nUnable to open file: \'%s.json\'\n" % file_name)
exit()
element = input("\nWhat name are we looking for? ")
print ("")
element_found = advanced_search(data, element) # Set the value of this boolean
variable as a result of a function
if element_found == True:
print ("SUCCESS! - We found \"%s\" in \'%s.json\' - SUCCESS!" % (element,
file_name))
exit()
else:
print ("FAIL! - \"%s\" not found in \'%s.json\' - FAIL!" % (element,
file_name))
exit()
# 1. Name:
# Sergio Henrique
# 2. Assignment Name:
# Lab 08: Sort
# 3. Assignment Description:
# This progrmas reads a json file and sorts its elements
# 4. What was the hardest part? Be as specific as possible.
# Converting a typical C++ for loop into a python loop inside the function (I
#used
# a while loop instead). Also, find out how to display each element of the
#file on a distinct line.
# Including asserts as a code, not as a commentary or as an if statement, was
#a little tricky too.
# 5. How long did it take for you to complete the assignment?
# 5h
import json
def sorting(list, file_name):
i = len(list['array']) - 1
#Make sure the file is not empty or, for some reason, has negative values
assert i >= 0, "\nERROR: File \'%s.json\'\n is empty" % file_name
print ("\nHere is the original array:")
print ("%s\n" % data['array'])
while i >= 1: #A
pivot = i - 1 #B
while pivot >= 0: #C
if list['array'][pivot] > list['array'][i]: #D
temp_v = list['array'][pivot]
list['array'][pivot] = list['array'][i]
list['array'][i] = temp_v
pivot -= 1
i -= 1
print ("Now, here is the sorted array:")
for loop in list['array']:
print ("\t%s" % loop) #E
#----------------------------------------------------
file_name = input("\nWhat is the name of the file? ")
try:
with open("%s.json" % file_name) as JasonVoorhees: # Added the file type
data = json.load(JasonVoorhees)
#Assert: Use a try/except to make sure the file was read succesfully
# The user don't have to type the file type, if so, the program will not
find the file
# He/she will see the problem when the exit message show up
except:
exit("\nUnable to open file: \'%s.json\'\n" % file_name)
sorting(data, file_name)

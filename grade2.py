print ""
# prompt
#------------------------------------------
grade = int(input("What was your score (0 to 100): "))
#------------------------------------------

print ""

# calcs table
#--------------------------
if grade >= 93:
  print "Your grade is a A , congratulations!!!"
elif grade >= 90:
  print "Your grade is a A- , outstanding!!"
elif grade >= 87:
  print "Your grade is a B+ , excelent! "
elif grade >= 83:
  print "Your grade is a B , nice!"
elif grade >= 80:
  print "Your grade is a B- , good."
elif grade >= 77:
  print "Your grade is a C+ , ok?"
elif grade >= 73:
  print "Well... Your grade is a C"
elif grade >= 70:
  print "Your grade is a C- , you could do better"
elif grade >= 67:
  print "Your grade is a D+ , need a help huh?"
elif grade >= 63:
  print "Your grade is a D , what happened?"
elif grade >= 60:
  print "Your grade is a D- , really!? That's all you got?"
else:
  print "Your grade is a F , are you serious!?"
#--------------------------
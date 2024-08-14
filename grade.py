count = 0
total = 0
numScores = 5

while count < numScores:
  score = int(input("What was your score (0 to 100): "))
  count +=1
  total += score
  
avgScore = total / numScores
print 
if avgScore >= 93:
  print "Your average score is " + str(avgScore) + ", you got an A, congratulations!!!"
elif avgScore >= 90:
  print "Your average score is " + str(avgScore) + " Your average grade is a A- , outstanding!!"
elif avgScore >= 87:
  print "Your average score is " + str(avgScore) + "Your average grade is a B+ , excelent! "
elif avgScore >= 83:
  print "Your average score is " + str(avgScore) + " Your average grade is a B , nice!"
elif avgScore >= 80:
  print "Your average score is " + str(avgScore) + " Your average grade is a B- , good."
elif avgScore >= 77:
  print "Your average score is " + str(avgScore) + " Your average grade is a C+ , ok?"
elif avgScore >= 73:
  print "Your average score is " + str(avgScore) + " Well... Your average grade is a C"
elif avgScore >= 70:
  print "Your average score is " + str(avgScore) + " Your average grade is a C- , you could do better"
elif avgScore >= 67:
  print "Your average score is " + str(avgScore) + " Your average grade is a D+ , need a help huh?"
elif avgScore >= 63:
  print "Your average score is " + str(avgScore) + " Your average grade is a D , what happened?"
elif avgScore >= 60:
  print "Your average score is " + str(avgScore) + " Your average grade is a D- , really!? That's all you got?"
else:
  print "Your average score is " + str(avgScore) + " Your average grade is a F, see you next semester >:D"
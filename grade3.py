def returnLetterGrade (numGrade):
    if numGrade >= 93:
        return "A"
    elif numGrade >= 90:
        return "A-"
    elif numGrade >= 87:
        return "B+"
    elif numGrade >= 83:
        return "B"
    elif numGrade >= 80:
        return "B-"
    elif numGrade >= 77:
        return "C+"
    elif numGrade >= 73:
        return "C"
    elif numGrade >= 70:
        return "C-"
    elif numGrade >= 67:
        return "D+"
    elif numGrade >= 63:
        return "D"
    elif numGrade >= 60:
        return "D-"
    else:
        return "F"
        
gradeMath = int(input("Enter a grade for Math: "))
letterMath = returnLetterGrade (gradeMath)
gradeEnglish = int(input("Enter a grade for English: "))
letterEnglish = returnLetterGrade (gradeEnglish)
gradePE = int(input("Enter a grade for PE: "))
letterPE = returnLetterGrade (gradePE)
gradeScience = int(input("Enter a grade for Science: "))
letterScience = returnLetterGrade (gradeScience)
gradeArt = int(input("Enter a grade for Art: "))
letterArt = returnLetterGrade (gradeArt)
print ""
print "Your Math score is %i, you got a %s" % gradeMath, letterMath
print "Your English score is %i, you got a %s" % gradeEnglish, letterEnglish
print "Your PE score is %i, you got a %s" % gradePE, letterPE
print "Your Science score is %i, you got a %s" % gradeScience, letterScience
print "Your Art score is %i, you got a %s" % gradeArt, letterArt

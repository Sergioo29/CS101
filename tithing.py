print "This is a variation of the Budget program, but this one adds your tithing for you"
print ""


# Income and Commandments
moneyEarned = float(input("Enter your monthly cash blessings: "))

tithing = moneyEarned * 0.10

fast = float(input("Enter how much you would like to pay for fast offerings: "))




# The Other Prompts
in1 = input("Enter Item 1: ")
m1 = float(input("Enter Item 1 Monthly Amount: "))

in2 = input("Enter Item 2: ")
m2 = float(input("Enter Item 2 Monthly Amount: "))

in3 = input("Enter Item 3: ")
m3 = float(input("Enter Item 3 Monthly Amount: "))

in4 = input("Enter Item 4: ")
m4 = float(input("Enter Item 4 Monthly Amount: "))

in5 = input("Enter Item 5: ")
m5 = float(input("Enter Item 5 Monthly Amount: "))



# The Budget
print ""
print ""
print "Personal Budget"

column1 = "Item"
column2 = "Month"
column3 = "Year"
column4 = "Income"

print "========================================"
print "%s\t\t%s\t\t%s" % (column4, column2, column3)
print "========================================"

yIncome = moneyEarned * 12 
print  "\t\t%.2f \t\t$ %.2f" % (moneyEarned, yIncome)

print "========================================"
print "%s\t\t%s\t\t%s" % (column1, column2, column3)
print "========================================"

yTithing = tithing * 12
print "Tithing \t$ %.2f \t$ %.2f" % (tithing, yTithing)

yFast = fast * 12
print "Fast Off \t$ %.2f \t$ %.2f" % (fast, yFast)

y1 = m1 * 12
print "%s \t\t$ %.2f \t$ %.2f" % (in1, m1, y1)

y2 = m2 * 12
print "%s\t\t$ %.2f \t$ %.2f" % (in2, m2, y2)

y3 = m3 * 12
print "%s\t\t$ %.2f \t$ %.2f" % (in3, m3, y3)

y4 = m4 * 12
print "%s\t\t$ %.2f \t$ %.2f" % (in4, m4, y4)

y5 = m5 * 12
print "%s\t\t$ %.2f \t$ %.2f" % (in5, m5, y5)

i6 = "Savings"
print "========================================="
print "%s\t\t%s\t\t%s" % (i6, column2, column3)
print "========================================="
m6 = moneyEarned - tithing - fast - m1 - m2 - m3 - m4 - m5
y6 = yIncome - yTithing - yFast - y1 - y2 - y3 - y4 - y5
print "   \t\t$ %.2f\t$ %.2f" % (m6, y6)

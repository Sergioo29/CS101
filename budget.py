# The part 1 test
x = 1 + 1
y = 2 + x
print y

print "%s/t%"

# The Budget
print "Monthly Budget"

column1 = "Item"
column2 = "Month"
column3 = "Year"
print "========================================"
print "%s\t\t%s\t\t%s" % (column1, column2, column3)
print "========================================"

i1 = "Movies"
m1 = 12
y1 = m1 * 12
print "%s \t\t$ %.2f \t$ %.2f" % (i1, m1, y1)

i2 = "Tithing"
m2 = 15
y2 = m2 * 12
print "%s \t$ %.2f \t$ %.2f" % (i2, m2, y2)

i3 = "Video-games"
m3 = 20
y3 = m3 * 12
print "%s \t$ %.2f \t$ %.2f" % (i3, m3, y3)

i4 = "Health"
m4 = 40
y4 = m4 * 12
print "%s \t\t$ %.2f \t$ %.2f" % (i4, m4, y4)

i5 = "Food"
m5 = 60
y5 = m5 * 12
print "%s \t\t$ %.2f \t$ %.2f" % (i5, m5, y5)

i6 = "Rent"
m6 = 50
y6 = m6 * 12
print "%s \t\t$ %.2f \t$ %.2f" % (i6, m6, y6)

print "========================================="
i7 = "Total"
m7 = m1 + m2 + m3 + m4 + m5 + m6
y7 = y1 + y2 + y3 + y4 + y5 + y6
print "%s \t\t$ %.2f \t$ %.2f" % (i7, m7, y7)

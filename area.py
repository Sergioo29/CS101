import math

# Add your code here
pi = 3.141592

def displayWelcome():
  print ""
  print "Welcome to my area and perimeter calculator"
  print "=========================================="

def calcAreaCircle(radius):
  area = pi * radius ** 2
  return area

def calcPerimeterCircle(radius):
  perimeter = 2 * pi * radius
  return perimeter

def calcAreaSquare(side):
  area = side * side
  return area

def calcPerimeterSquare(side):
  perimeter = side * 4
  return perimeter

def calcAreaRect(width, height):
  area = width * height
  return area

def calcPerimeterRect(width, height):
  perimeter = width * 2 + height * 2
  return perimeter

def calcAreaTriangle(base, height):
  area = base * height / 2
  return area

# =====================================================================

# Main Code - DO NOT EDIT ANYTHING BELOW.  Add your functions above

displayWelcome()


radius = 3.56

area = calcAreaCircle(radius)

perimeter = calcPerimeterCircle(radius)

print('Circle   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


side = 9.23

area = calcAreaSquare(side)

perimeter = calcPerimeterSquare(side)

print('Square   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


width = 2.9

height = 14.22

area = calcAreaRect(width, height)

perimeter = calcPerimeterRect(width, height)

print('Rectangle: area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


base = 7.97

height = 5.31

area = calcAreaTriangle(base, height)

print('Triangle : area = {0:.2f}'.format(area))
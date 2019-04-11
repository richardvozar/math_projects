import math
a = int(input("Mi az 'a': "))
b = int(input("Mi a 'b': "))
c = int(input("Mi a 'c': "))
diszkriminans = b**2-4*a*c
x1 = (-(b) + math.sqrt(diszkriminans))/2*a
x2 = (-(b) - math.sqrt(diszkriminans))/2*a
print('x1 = ' + str(x1))
print('x2 = ' + str(x2))

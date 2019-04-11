a, b = 0, 1
for i in range(20):
    a, b = b, a+b
    print(a)


if a > 999:
    print('Az első 4 számjegyű fibonacci szám a ' + str(i-2) + '. helyen van.')

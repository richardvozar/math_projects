# try to make a sorting algorithm...
# ...
# okay
from random import randint as rint

# bubble sort i guess
def doSort(num):
    for r in range(len(num)):
        for i in range(len(num)-1):
            if num[i] > num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]

# testing
randoms=[]
for k in range(100):
    randoms.append(rint(1,1000))

doSort(randoms)
print(randoms)

# ---------------------------------------------------------------------------------------- #

# something else to create
def doSort2(num2):
    pass
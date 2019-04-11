num = int(input('How many fib numbers do you want? '))
a=0
b=1
print(a,b, end=' ')
for i in range(num):
    a = a+b
    b = a+b
    print(a,b, end=' ')

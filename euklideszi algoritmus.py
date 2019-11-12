def euclid(a, b):
    if b>a:
        a, b = b, a
    # m -> maradek
    m = a%b
    while m>0:
        m = a%b
        a, b = b, m
        if m==0:
            print(a)
euclid(360, 225)

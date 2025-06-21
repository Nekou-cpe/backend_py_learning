def factoriel(n):
    f=1
    for i in range(n,1,-1):
        f*=i
    return f

factoriel(10)

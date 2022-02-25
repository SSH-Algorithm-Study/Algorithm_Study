def fibo_func(n):
    if n < 2:
        return n

    if fibo[n]:
        return fibo[n]

    fibo[n] = fibo_func(n-1) + fibo_func(n-2)
    return fibo[n]

n = eval(input())
fibo = [None] * (n+1)
print(fibo_func(n))
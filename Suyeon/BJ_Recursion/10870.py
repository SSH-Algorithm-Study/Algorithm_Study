# def fibo_func(n):
#     if n < 2:
#         return n
#
#     if fibo[n]:
#         return fibo[n]
#
#     fibo[n] = fibo_func(n-1) + fibo_func(n-2)
#     return fibo[n]
#
# n = eval(input())
# fibo = [None] * (n+1)
# print(fibo_func(n))

n = eval(input())
fibo = [None] * (n + 1)

for i in range(n + 1):
    if i < 2:
        fibo[i] = i
    else:
        fibo[i] = fibo[i - 1] + fibo[i - 2]

print(fibo[n])
num = eval(input())
swith = list(map(eval,input().split()))

ex = sum(swith)  # 켜진 기존전구 개수 기댓값
ey = 0   # 켜진 추가전구 개수 기댓값

for i in range(num-1):
    ey = ey + swith[i]*(1-swith[i+1]) + (1-swith[i]) * swith[i+1]

print(ex + ey)




import math

num, boxs = input().split()
num = int(num)
boxs = int(boxs)
v_list = list(map(int,input().split()))
v_list.sort()
print(v_list)
max_vt = 0
for i in range(num-1):
    vt = v_list[0] * (i+1) + v_list[i+1] * (num-i-1)
    print(vt)
    max_vt = max(max_vt, vt)


print(math.ceil(boxs/max_vt))





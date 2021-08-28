import math

num, boxs = tuple(map(int,input().split()))
v_list = list(map(int,input().split()))

v_list.sort()
i = 0
if num > 2 :
    vt1 = v_list[0] * (num//2) + v_list[num//2] * (num-(num//2))
    vt2 = v_list[0] * (num//2+1) + v_list[num//2+1] * (num-(num//2)-1)
    vt = max(vt2,vt1)
else:
    vt = v_list[0] * (num//2) + v_list[num//2] * (num-(num//2))
print(math.ceil(boxs/vt))




# num, boxs = tuple(map(int,input().split()))
# v_list = list(map(int,input().split()))
# v_list.sort()
# i = 0
# max_vt = 0
# while i < num-1:
#     vt = v_list[0] * (i+1) + v_list[i+1] * (num-i-1)
#     max_vt = max(max_vt, vt)
#     i += 1
#
# print(math.ceil(boxs/max_vt))





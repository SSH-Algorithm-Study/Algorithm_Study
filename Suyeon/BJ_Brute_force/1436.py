N = int(input())

# result = ['6','6','6']
#
# for c in str(N-1):
#     result.append(c)
#
# result.sort() # 정렬
# if result[0] == 0: # 맨 앞자리가 0일때 예외처리
#     i = 0
#     while result[i] != 0:
#         i += 1
#     result[0], result[i] = result[i], result[0]
#
# print("".join(result))

i = 0
number = 666

while i < N:
    if "666" in str(number):
        i += 1
    number += 1
print(number-1)
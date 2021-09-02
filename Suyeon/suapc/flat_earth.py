def flat_earth(earth, sec):
    start = earth - sec
    if start < 0:   # 음수일 때 예외처리
        start = 0
    block = (4*start + 4*earth) * (earth-start+1)
    return block//2


#
# result = []
# num = eval(input())
#
# for _ in range(num):
#     earth, sec = input().split()
#     result.append(flat_earth(int(earth), int(sec)))
#
# for res in result:
#     print(res)


num = eval(input())

for _ in range(num):
    earth, sec = input().split()
    print(flat_earth(int(earth), int(sec)))

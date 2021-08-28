import collections

request, bus = tuple(map(int,input().split()))
requests = []
buses = []
count = 0

for _ in range(request):
    x= list(map(int, input().split()))
    requests.append(x)


for _ in range(bus):
    x = list(map(int, input().split()))
    x.append(0)
    buses.append(x)

requests.sort(key=lambda x : (x[0], x[1]))
buses.sort(key=lambda x: (x[0], x[1]))

point = 0

for r in requests:
    for i in range(point, len(buses)):
        if buses[i][0] >= r[0] and buses[i][1] <= r[1] and buses[i][2] == 0:
            buses[i][2] = 1
            count += 1
            point = i+1
            break


print(count)


# request, bus = tuple(map(int,input().split()))
# requests = []
# buses = collections.defaultdict(list)
# count = 0
#
# for _ in range(bus):
#     x = list(map(int, input().split()))
#     x.append(0)
#     buses[x[0]].append(x)
#
# for _ in range(request):
#     x= list(map(int, input().split()))
#     requests.append(x)
#
# for r in requests:
#     find = 0
#     for key in buses.keys():
#         if find != 0:
#             break
#         if key < r[0]:
#             continue
#         for b in buses[key]:
#             if r[1] >= b[1] and b[2] == 0:
#                 b[2] = 1
#                 count += 1
#                 find = 0
#                 break
#
#
#
# print(count)
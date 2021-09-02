# request, bus = input().split()
# requests = []
# buses = []
# count = 0
#
# for _ in range(int(request)):
#     x = input().split()
#     requests.append(x)
#
#
# for _ in range(int(bus)):
#     x = input().split()
#     buses.append(x)
#
# requests.sort(key=lambda x : (x[0], x[1]))
# buses.sort(key=lambda x: (x[0], x[1]))
#
# point = 0
#
# for r in requests:
#     while point < len(buses):
#         if buses[point][0] >= r[0] and buses[point][1] <= r[1]:
#             count += 1
#             point = point + 1
#             break
#         point = point + 1
#     if point >= len(buses):
#         break
#
#
# print(count)





request, bus = input().split()
requests = []
buses = []
count = 0

for _ in range(int(request)):
    x = input().split()
    requests.append(x)


for _ in range(int(bus)):
    x = input().split()
    buses.append(x)

requests.sort(key=lambda x : x[0])
buses.sort(key=lambda x: x[0])

for r in requests:
    i = 0
    j = 0
    while i < len(buses) and buses[i][0] < r[0]:
        i += 1
    if i >= len(buses):
        break
    bus_list = sorted(buses[i:], key=lambda x:x[1])
    while j < len(bus_list) and bus_list[j][1] > r[1]:
        j += 1
    if j >= len(bus_list):
        break
    count += 1
    buses.remove([bus_list[j][0], bus_list[j][1]])


print(count)



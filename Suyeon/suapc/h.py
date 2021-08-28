import collections

num, x = tuple(map(int,input().split()))
c_list = list(map(int,input().split()))

count = c_list.count(x)
c_list = list(filter(lambda a: a != x, c_list))

c_list.sort()
deque = collections.deque()
for c in c_list:
    deque.append(c)

while len(deque) > 1:
    res = min(deque.popleft() + deque.pop() + x/2 , x)
    if res >= x:
        count += 1
    else:
        deque.append(res)



print(count)

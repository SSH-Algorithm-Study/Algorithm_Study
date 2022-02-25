count = 0
msg = []

def hanoi(num,start,mid,finish):
    global count
    if num == 1:
        msg.append("%d %d" %(start,finish))
        count += 1
    else:
        hanoi(num-1,start,finish,mid)
        msg.append("%d %d" %(start,finish))
        count += 1
        hanoi(num-1,mid,start,finish)

n = eval(input())
hanoi(n,1,2,3)

print(count)
for m in msg:
    print(m)

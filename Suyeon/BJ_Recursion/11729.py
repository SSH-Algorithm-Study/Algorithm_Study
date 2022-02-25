count = 0
msg = []

def hanoi(num,start,mid,finish):
    global count
    if num == 1:
        msg.append((start,finish)) # n이 하나면 경유 없이 바로 finish로 옮기기
        count += 1
    else:
        hanoi(num-1,start,finish,mid) # n-1개 원판 2번째로 옮기기
        msg.append((start,finish)) # n번째 원판 3번째로 옮기기
        count += 1
        hanoi(num-1,mid,start,finish) # n-1개 원판 3번째로 옮기기

n = eval(input())
hanoi(n,1,2,3)

# 출력
print(count)
for m in msg:
    print(*m) # 튜플 언팩

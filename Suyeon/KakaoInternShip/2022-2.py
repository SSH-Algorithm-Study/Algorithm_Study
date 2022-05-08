import collections


def solution(queue1, queue2):
    deque1 = collections.deque()
    deque2 = collections.deque()
    sum1 = 0
    sum2 = 0
    for num in queue1:
        sum1 += num
        deque1.append(num)
    for num in queue2:
        sum2 += num
        deque2.append(num)

    length = len(deque1)
    zero = 0
    count = 0



    while zero < 1 or count < length * 2:
        if len(deque1):
            return -1
        if len(deque2):
            return -1
        if sum1 == sum2:
            return count
        elif sum1 > sum2:
            if sum2 == 0:
                zero += 1
            sum2 += deque1[0]
            sum1 -= deque1[0]
            deque2.append((deque1.popleft()))
            count += 1
        else:
            if sum1 == 0:
                zero += 1
            sum1 += deque2[0]
            sum2 -= deque2[0]
            deque1.append((deque2.popleft()))
            count += 1

    return -1

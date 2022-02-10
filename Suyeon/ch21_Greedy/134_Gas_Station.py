class Solution:
    def canCompleteCircuit(self, gas , cost) -> int:
        size = len(gas)
        sub_list = [ gas[i] - cost[i] for i in range(size)]

        # 예외처리
        if sum(sub_list) < 0 :
            return -1
        if len(sub_list) == 1:
            return 0


        #시작점
        head, tail = size-1, size-1
        total = sub_list[head]

        while tail - head != size-1:
            if total >= 0:
                tail += 1
                total += sub_list[tail % size]
            else:
                head -= 1
                total += sub_list[head]


        return head


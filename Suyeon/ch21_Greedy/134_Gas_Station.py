class Solution:
    def canCompleteCircuit(self, gas , cost) -> int:
        size = len(gas)
        sub_list = [ gas[i] - cost[i] for i in range(size)] # 차액계산

        # 예외처리
        if sum(sub_list) < 0 :
            return -1
        if len(sub_list) == 1:
            return 0


        #시작점
        head, tail = size-1, size-1
        total = sub_list[head]

        while tail - head != size-1: # 사이즈가 다다르면 끝
            if total >= 0: # 차액이 음수가 아니면 : 유지
                tail += 1
                total += sub_list[tail % size]
            else: # 차액이 음수이면 : 시작점 옮기기
                head -= 1
                total += sub_list[head]


        return head


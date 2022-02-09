import heapq
import collections


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        pq = []  # 현재 가능한 일
        freqs = dict(collections.Counter(tasks))
        waitQ = collections.deque()  # 대기큐
        time = 0

        for freq in freqs:
            pq.append((-freqs[freq], freq))

        heapq.heapify(pq)  # 우선순위큐에 한번에 넣기


        while sum(freqs.values()) != 0:
            print(waitQ)
            if waitQ:
                task = waitQ.popleft()

                if (task != "#"):
                    heapq.heappush(pq, (-freqs[task], task))
            print(pq)
            if pq:  # 할일 있음
                task = heapq.heappop(pq)
                freqs[task[1]] -= 1
                print(task[1])
                if freqs[task[1]] != 0:  # 남은 일이라면 waitQ에 넣기
                    while len(waitQ) < n:  # 앞에 최소 n개의 일이 있도록
                        waitQ.append('#')
                    waitQ.append(task[1])

            else:  # 할일 없음
                waitQ.append('#')
                print("#")

            time += 1
            print("=======================================")
        return time

sol = Solution()
print(sol.leastInterval(["A","A","A","A","A","B","C","D","E","F","G"],2))

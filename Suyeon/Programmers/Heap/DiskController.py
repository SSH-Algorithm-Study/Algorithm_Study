# 처음에 들어온 작업부터 시작
# 작업 끝날 때까지 들어온 작업들 길이순으로 저장 -> PQ
import heapq

def solution(jobs):
    answer = 0

    N = len(jobs)
    jobs.sort() # 들어온 순서대로 정렬
    working = False
    time = jobs[0][0]
    waiting = []
    work = 0 # 주어진 일양
    start = 0 # 현재 일이 주어진 시간
    job = jobs.pop(0)
    heapq.heappush(waiting, (job[1], job[0]))

    while jobs or waiting or working:
        if jobs and time == jobs[0][0]:
            job = jobs.pop(0)
            heapq.heappush(waiting, (job[1], job[0]))

        if not working and waiting: # 쉬는중
            work, start = heapq.heappop(waiting)
            working = True

        if working: # 일하는 중
            work -= 1
            if work == 0: # 일 끝
                working = False
                print(time-start+1)
                answer += time - start + 1

        time += 1



    return answer // N


print(solution([[2, 3], [6,4], [8, 12]]))
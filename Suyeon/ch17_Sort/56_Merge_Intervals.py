class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        result = []

        intervals.sort()

        # 초기화
        first = intervals[i][0]
        last = intervals[i][1]
        
        while i < n-1 :
            i += 1
            if last >= intervals[i][0]:
                if last < intervals[i][1]:
                    last = intervals[i][1] # last 갱신
            else:
                result.append([first,last]) # 저장
                # 새로운 범위설정
                first = intervals[i][0]
                last = intervals[i][1]

        result.append([first,last]) # 마지막 끝난곳에서 추가

        return result






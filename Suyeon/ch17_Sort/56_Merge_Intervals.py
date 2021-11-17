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
                if last < intervals[i][1]:  # 엇갈리게 겹친느 경우
                    last = intervals[i][1] # last 갱신
            else: # 겹치는 부분 없는 경우
                result.append([first,last]) # 저장
                # 새로운 범위설정
                first = intervals[i][0]
                last = intervals[i][1]

        result.append([first,last]) # 마지막 끝난곳에서 추가

        return result


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        result = []

        intervals.sort()

        # 초기화
        first = intervals[i][0]
        last = intervals[i][1]

        while i < n - 1:
            i += 1
            ######### max활용으로 if문 줄이기
            if last >= intervals[i][0]:
                last = max(last, intervals[i][1])

            #########
            else:  # 겹치는 부분 없는 경우
                result.append([first, last])  # 저장
                # 새로운 범위설정
                first = intervals[i][0]
                last = intervals[i][1]

        result.append([first, last])  # 마지막 끝난곳에서 추가

        return result




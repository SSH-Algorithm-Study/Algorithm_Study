class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        idx_stack = [0]
        result = [0] * len(temperatures)


        for i in range(len(temperatures)-1):
            while idx_stack and temperatures[idx_stack[-1]] < temperatures[i+1] :  # stack이 비어있지 않고 스택에 값보다 크면
                result[idx_stack.pop()] = (i+1) - idx_stack[-1]  # idx값 차이만큼 result값

            idx_stack.append(i+1)

        return result


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        idx_stack = [0]

        for i in range(len(temperatures) - 1):
            while idx_stack and temperatures[idx_stack[-1]] < temperatures[i + 1]:
                temperatures[idx_stack[-1]] = (i + 1) - idx_stack[-1]
                idx_stack.pop()

            idx_stack.append(i + 1)

        while idx_stack:
            temperatures[idx_stack.pop()] = 0
        return temperatures




            


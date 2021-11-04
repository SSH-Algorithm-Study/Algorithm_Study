class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]

        if n > 2:
            for i in range(2, n):
                dp.append(dp[i - 1] + dp[i - 2]) # 마지막이 2칸일때와 1칸일때의 경우 더하기

        return dp[n - 1]

import collections

# 메모이제이션
class Solution:
    def fib(self, n: int) -> int:
        dp = [None] * (n + 1)

        def fibo(n):
            if n <= 1:
                return n
            if dp[n]:
                return dp[n]  # dp에 저장된건 여기서만 이용함

            dp[n] = fibo(n - 1) + fibo(n - 2) # 리턴된 값들을 이용해서 연산

            return dp[n]   # 함수에서 현재 dp값 계산후 return 해줘야함

        return fibo(n)   # n=0일때 때문에 return dp[n]하면 안된다


class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.dp[n]



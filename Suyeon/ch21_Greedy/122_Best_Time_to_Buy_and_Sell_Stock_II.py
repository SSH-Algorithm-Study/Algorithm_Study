import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit = 0
        total = 0

        for price in prices:
            min_price = min(price, min_price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

            if max_profit > profit:  # 하락세로 바뀌는 지점 : 이익 저장해주고 초기화
                min_price = price
                total += max_profit
                max_profit = 0


        return total + max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i-1]

        return total




def maxProfit(prices) -> int:
    max_price = 0
    min_time = 0
    time = 1

    while time < len(prices) - 2:
        if prices[time] < prices[min_time] and prices[time] < prices[time + 1]:
            max_price = max(max_price, sorted(prices[time + 1:])[-1] - prices[time])
            min_time = time

        time += 1


    return max_price

print(maxProfit([7,1,5,3,6,4]))


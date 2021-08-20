import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_dict = collections.defaultdict(int)
        result = 0

        for stone in stones:  # stone들 개수 파악
            stone_dict[stone] += 1

        for jewel in jewels:
            # if stone_dict[jewel] > 0: # stone에 jewel이 있다면
            #     result += stone_dict[jewel]  # 갯수더해주기
            result += stone_dict[jewel]  # 없는 경우 0이 더해지기때문에 분별할 필요 없음

        return result
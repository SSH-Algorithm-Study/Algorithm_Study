class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        return sum(map(int,(bin(x^y)[2:])))


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        return bin(x^y).count("1")
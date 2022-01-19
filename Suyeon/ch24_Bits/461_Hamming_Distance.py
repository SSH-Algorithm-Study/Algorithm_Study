class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        return sum(map(int,(bin(x^y)[2:])))
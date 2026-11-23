class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        power = 1
        while power < n:
            power *= 4
        return power == n

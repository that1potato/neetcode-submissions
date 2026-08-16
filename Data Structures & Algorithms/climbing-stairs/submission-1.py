class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        w = [0] * n
        w[0], w[1] = 1, 2
        for i in range(2, n):
            w[i] = w[i - 1] + w[i - 2]
        return w[-1]
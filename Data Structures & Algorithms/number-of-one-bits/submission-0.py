class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 0x00000001
        count = 0
        for i in range(32):
            if mask & n == mask:
                count += 1
            mask = mask << 1
        return count
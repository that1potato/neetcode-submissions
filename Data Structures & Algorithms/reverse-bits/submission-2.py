class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 0x00000001
        out = 0x00000000
        for i in range(32):
            out = out << 1
            out = out | (mask & n)
            n = n >> 1
        return out
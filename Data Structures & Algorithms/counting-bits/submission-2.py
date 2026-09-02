class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]
        bit = 0
        for i in range(1, n+1):
            count = output[i - 2**bit] + 1
            output.append(count)
            if i % 2**bit == 0:
                bit += 1
        return output
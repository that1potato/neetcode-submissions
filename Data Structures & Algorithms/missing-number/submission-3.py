class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [i for i in range(len(nums) + 1)] + nums
        xor_result = arr[0]
        for n in arr[1:]:
            xor_result ^= n
        return xor_result
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        entries = set()
        for n in nums:
            entries.add(n)
        for i in range(len(nums)):
            if i not in entries:
                return i 
        return len(nums)
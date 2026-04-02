class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_set = {}
        for num in nums:
            if not num in freq_set:
                freq_set[num] = 1
            else:
                return True
        return False
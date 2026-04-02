class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seen = set()

        def fetch(n, count):
            seen.add(n)
            if n + 1 not in nums_set:
                return count
            return fetch(n + 1, count + 1)
        
        max_len = 0
        for n in nums:
            if n in seen:
                continue
            length = fetch(n, 1)
            max_len = length if length > max_len else max_len
        return max_len

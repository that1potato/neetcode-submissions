class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        out = []
        i = 0
        while i < len(nums) - 2:
            n = nums[i]
            if n > 0:
                break
            j = i + 1
            while j < len(nums) - 1:
                m = nums[j]
                temp = [n]
                target = 0 - n - m
                if target in nums[j + 1:]:
                    temp.append(m)
                    temp.append(target)
                    out.append(temp) if temp not in out else None
                    #i = nums[j + 1:].index(target) + j + 1
                j += 1
            i += 1
        return out
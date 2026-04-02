class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for n in nums:
            if n != 0:
                product *= n
            else:
                zeros += 1
        
        out = [0] * len(nums)
        if zeros > 1:
            return out
        
        for i in range(len(nums)):
            if nums[i] == 0:
                out[i] = product if zeros == 1 else 0
            else:
                out[i] = int(product / nums[i]) if zeros == 0 else 0
        
        return out

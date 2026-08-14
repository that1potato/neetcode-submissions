class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def dfs(addends, index):
            if sum(addends) == target:
                output.append(addends)
                return
            elif sum(addends) > target:
                return
            
            # prevent duplication
            for i in range(index, len(nums)):
                dfs(addends + [nums[i]], i)
            return 
        
        for i, n in enumerate(nums):
            dfs([n], i)
        return output

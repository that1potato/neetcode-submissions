class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def dfs(addends, index, total):
            if total == target:
                output.append(addends)
                return
            elif total > target:
                return
            
            # prevent duplication
            for i in range(index, len(nums)):
                dfs(addends + [nums[i]], i, total + nums[i])
            return 
        
        
        dfs([], 0, 0)
        return output

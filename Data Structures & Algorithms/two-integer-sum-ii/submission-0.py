class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_set = set(numbers)
        for n in numbers:
            if target - n in nums_set:
                break
        return [numbers.index(n) + 1, numbers.index(target - n) + 1]
        
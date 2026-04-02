class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = max(piles)
        while l <= r:
            mid = (l + r) // 2
            k = mid
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i] / k)
            
            if time <= h:
                min_k = min(min_k, k)
                r = mid - 1
            else:
                l = mid + 1
    
        return min_k
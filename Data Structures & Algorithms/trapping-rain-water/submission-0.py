class Solution:
    def trap(self, height: List[int]) -> int:
        water = [0] * len(height)

        # scan right
        idx = 0
        max_height = 0
        while idx < len(height):
            max_height = max(height[idx], max_height)
            water[idx] = max_height
            idx += 1
        
        # scan left
        idx = len(height) - 1
        max_height = 0
        while idx >= 0:
            max_height = max(height[idx], max_height)
            water[idx] = min(max_height, water[idx])
            idx -= 1
        
        out = 0
        for i, w in enumerate(water):

            if w - height[i] > 0:
                out = out + w - height[i] 
        return out
    
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        nof = 0
        time = 0.0
        for p, s in pair:
            curTime = (target - p) / s
            if curTime > time: 
                nof += 1
                time = curTime
        return nof
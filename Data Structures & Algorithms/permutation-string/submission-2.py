class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def freq(s):
            out = {}
            for c in s:
                if c not in out:
                    out[c] = 1
                else:
                    out[c] += 1
            return out
    
        l = 0
        for r in range(len(s2) + 1):
            if r - l == len(s1):
                if freq(s1) == freq(s2[l:r]):
                    return True
                l += 1
        return False

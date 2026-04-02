class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        def get_idx(c):
            return ord(c) - ord('a')
        
        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(len(s1)):
            s1_count[get_idx(s1[i])] += 1
            window_count[get_idx(s2[i])] += 1
            
        for i in range(len(s2) - len(s1)):
            if s1_count == window_count:
                return True
            
            window_count[get_idx(s2[i + len(s1)])] += 1
            window_count[get_idx(s2[i])] -= 1
            
        return s1_count == window_count

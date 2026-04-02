class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        max_len = 0
        for c in s:
            if c in window:
                max_len = max(max_len, len(window))
                window = window[window.index(c) + 1:]
            window.append(c)
        
        return max(max_len, len(window))
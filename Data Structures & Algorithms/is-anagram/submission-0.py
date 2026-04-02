class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet_s = {}
        for c in s:
            if c not in alphabet_s:
                alphabet_s[c] = 1
            else:
                alphabet_s[c] += 1
    
        alphabet_t = {}
        for c in t:
            if c not in alphabet_t:
                alphabet_t[c] = 1
            else:
                alphabet_t[c] += 1
        
        return alphabet_s == alphabet_t

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def to_freq(word):
            freq = {}
            for c in word:
                if c not in freq:
                    freq[c] = 1
                else: 
                    freq[c] += 1
            return freq

        seen = []
        out = []
        for word in strs:
            word_freq = to_freq(word) 
            if word_freq not in seen:
                seen.append(word_freq)
                out.append([word])
                continue

            idx = seen.index(word_freq)
            out[idx].append(word)
        return out
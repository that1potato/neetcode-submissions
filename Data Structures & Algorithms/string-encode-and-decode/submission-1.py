class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for s in strs:
            string += s
            string += '<EOS> '
        return string

    def decode(self, s: str) -> List[str]:
        out = []
        temp = ''
        for c in s:
            temp += c
            if temp[-6:] == '<EOS> ':
                out.append(temp[:-6])
                temp = ''
        return out

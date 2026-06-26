class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += f'{len(i)}' + "#" + i
        return s
        

    def decode(self, s: str) -> List[str]:
        l = []
        while len(s) != 0:
                i = s.index("#")
                length = int(s[:i])
                word = s[i+1:length+1+i]
                l.append(word)
                s = s[length+1+i:]
        return l
                    


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for value in strs:
            key = "".join(sorted(value))
            if key not in d:
                d[key] = [value]
            else:
                d[key].append(value)
        l = []
        for key,value in d.items():
            l.append(value)
        return l
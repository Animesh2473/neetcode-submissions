class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        if len(s) != len(t):
            return False
        for x,y in zip(s,t):
            if x in ds:
                ds[x] += 1
            else:
                ds[x] = 0
            if y in dt:
                dt[y] += 1
            else:
                dt[y] = 0
        return ds == dt

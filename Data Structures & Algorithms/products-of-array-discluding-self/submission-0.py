import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f = []
        for i in nums:
            l = nums.copy()
            l[l.index(i)] = 1
            result = math.prod(l)
            f.append(result)
        return f
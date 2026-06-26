
def multi(l):
    result = 1
    for x in l:
        result *= x
    return result

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f = []
        for i in nums:
            l = nums.copy()
            l[l.index(i)] = 1
            result = multi(l)
            f.append(result)
        return f
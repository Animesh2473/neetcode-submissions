class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p,q = 0,1
        while p < len(numbers):
            if q == len(numbers):
                p += 1
                q = p+1
            elif numbers[p]+numbers[q] == target:
                return [p+1,q+1]
            else:
                q += 1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index,value in enumerate(nums):
            find = target - value
            if find in d:
                return [d[find],index]
            d[value] =  index
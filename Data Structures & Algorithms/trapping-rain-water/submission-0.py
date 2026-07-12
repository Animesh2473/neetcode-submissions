class Solution:
    def trap(self, height: List[int]) -> int:
        if not height :
            return 0

        left,right = 0,len(height)-1
        Leftmax,Rightmax = height[left],height[right]
        res = 0

        while left < right :
            if Leftmax < Rightmax:
                left+=1
                Leftmax = max(Leftmax,height[left])
                res += Leftmax - height[left]

            else:
                right -=1
                Rightmax = max(Rightmax,height[right])
                res += Rightmax - height[right]

        return res
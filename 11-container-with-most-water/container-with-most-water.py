class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        left = 0
        right = n-1
        max_val = 0
        while left<right:
            high = right - left
            length = min(height[right], height[left])
            ans = high*length
            
            if  ans> max_val:
                max_val = ans
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_val
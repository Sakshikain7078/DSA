class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)

        windowSum = 0
        for idx in range(k):
            windowSum += nums[idx]
        ans = windowSum
        for idx in range(k, N):
            windowSum = windowSum - nums[idx-k] + nums[idx]
            ans = max(ans, windowSum)
                
        return ans / k
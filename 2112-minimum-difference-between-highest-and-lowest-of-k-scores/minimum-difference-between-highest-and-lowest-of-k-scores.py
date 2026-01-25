class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = float('inf') 
        j = k-1
        for i in range(len(nums)-j):
            ans = min(ans,nums[i+j] - nums[i])
        return ans
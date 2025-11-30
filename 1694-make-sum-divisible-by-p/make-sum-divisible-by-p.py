class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem = sum(nums)%p
        if rem == 0:
            return 0
        mp = {}
        mp[0] = -1
        total = 0
        ans = len(nums)
        for ind, num in enumerate(nums):
            total = (total + num) % p
            remain = (total - rem + p) % p
            if remain in mp:
                ans = min(ans, ind-mp[remain])

            mp[total] = ind
        return ans if ans < len(nums) else -1
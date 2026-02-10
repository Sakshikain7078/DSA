class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        maxLen = 0
        for i in range(n):
            evenSet = set()
            oddSet = set()
            for j in range(i,n):
                if nums[j]%2 == 0:
                    evenSet.add(nums[j])
                else:
                    oddSet.add(nums[j])
                if len(evenSet) == len(oddSet):
                    curr = j-i+1
                    maxLen = max(curr,maxLen)
        return maxLen
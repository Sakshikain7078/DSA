class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if(i%3 == 0):
                count += 0
            if (i%3 == 2):
                count += 1
            if (i%3 == 1):
                count += 1
        return count
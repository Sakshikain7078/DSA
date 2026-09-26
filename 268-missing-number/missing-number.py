class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        # arr = set(range(0, n + 1))
        # miss = arr-set(nums)
        # return miss.pop()
        for i in range(n):
            if nums[i] != i:
                return i
        return n
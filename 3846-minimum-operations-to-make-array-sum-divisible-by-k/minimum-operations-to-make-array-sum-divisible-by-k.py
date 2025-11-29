class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)%k
        
        return total
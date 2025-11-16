class Solution:
    def jump(self, nums: List[int]) -> int:
        curr = 0
        far = 0
        jump = 0
        for i in range(len(nums)-1):
            far = max(far,nums[i]+i)
            if i == curr:
                curr = far
                jump += 1
        return jump
    
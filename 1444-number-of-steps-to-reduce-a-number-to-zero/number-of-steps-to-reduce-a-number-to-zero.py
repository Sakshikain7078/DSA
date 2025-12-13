class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        rem = num
        while rem != 0:
            if rem%2 == 0:
                rem = rem//2
            else:
                rem -= 1
            step += 1
        return step        
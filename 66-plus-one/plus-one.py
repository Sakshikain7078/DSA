class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # for i in range(len(digits)):
        #     if digits[-1] < 9:

        #         digits[-1] = digits[-1]+1
        #         return digits
        #     if digits[-1] == 9:
        #         return [1,0]

        digit = int("".join(map(str,digits)))
        digit += 1
        return [int(d) for d in str(digit)]
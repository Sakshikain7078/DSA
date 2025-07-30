class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        result = binary[2:]
        ones = result.count('1')
        return ones
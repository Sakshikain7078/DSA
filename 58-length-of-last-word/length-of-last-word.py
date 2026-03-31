class Solution:
    def lengthOfLastWord(self, s):
        x = s.split()
        a = x[-1]
        return len(a)
        
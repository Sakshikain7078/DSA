class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # res = []
        # for i in range(len(s)):
        #     if s[i] in t:
        #         res.append(s[i])
        #     else:
        #         return s[i]
        for i in t:
            if t.count(i)>s.count(i):
                return i
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # for i in range(len(s)-1):
        #     for j in range(i+1,len(s)):
        #         if s[i] == s[j]:
        #             return -1
        #         if s[i] != s[j]:
        #             return i
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1

                    
                
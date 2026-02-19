# class Solution:
#     def valid_str(self,s):
#         c_0=0
#         c_1=0
#         for ch in s:
#             if ch == '0':
#                 c_0 += 1
#             else:
#                 c_1 += 1
#         if c_0 != c_1:
#             return False
#         chan_count = 0
#         for i in range(1,len(s)):
#             if s[i] != s[i-1]:
#                 chan_count += 1
#         return chan_count == 1



#         # if c_0==c_1:
#         #     return True
#         # else:
#         #     False 
           
#     def countBinarySubstrings(self, s: str) -> int:
#         count = 0
#         for i in range(len(s)):
#             for j in range(i,len(s)):
#                 win=s[i:j+1]
#                 if self.valid_str(win):
#                     count+=1

#         return count    
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = prev = 0
        curr = 1
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                curr+=1
            else:
                result+=min(curr,prev)
                prev,curr = curr,1
        result += min(curr,prev)
        return result





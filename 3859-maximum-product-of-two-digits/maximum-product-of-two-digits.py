class Solution:
    def maxProduct(self, n: int) -> int:
        lis = list(map(int, str(n)))
        res = []
        for i in range(0,len(lis)-1):
            for j in range(i+1,len(lis)):
                ans = lis[i]*lis[j]
                res.append(ans)
        return max(res)
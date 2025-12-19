class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        sp = [strategy[i] * prices[i] for i in range(n)]
        

        baseline = sum(sp)
        h = k // 2
        old = sum(sp[:k])
        new = sum(prices[h:k])

        maxdiff = max(0, new - old)

        for r in range(k, n):
            l = r - k + 1  
            old += sp[r] - sp[l - 1]
            new += prices[r]
            new -= prices[l - 1 + h]
            maxdiff = max(maxdiff, new - old)

        return baseline + maxdiff
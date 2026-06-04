class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = sorted(score, reverse = True)
        ans = {}
        for rank, i in enumerate(res):
            if rank == 0:
                ans[i] = "Gold Medal"
            elif rank == 1:
                ans[i] = "Silver Medal"
            elif rank == 2:
                ans[i] = "Bronze Medal" 
            else:
                ans[i] = str(rank+1)
        return [ans[i] for i in score]
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        maxi = 0
        freq = Counter(nums)
        for i in freq:
            
            if i + 1 in freq:
                
                res = freq[i] + freq[i+1]
                maxi = max(maxi,res)
        return maxi

             
            
            
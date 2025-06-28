class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
    
    
        left_sum = sum(cardPoints[:k])
        maxi = left_sum
    
        right_sum = 0
    
    
        for i in range(1, k+1):
            left_sum -= cardPoints[k - i]       
            right_sum += cardPoints[-i]         
            maxi = max(maxi, left_sum + right_sum)
        
        return maxi

        
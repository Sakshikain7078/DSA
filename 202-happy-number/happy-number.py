class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            
            return True
        

        if n<10:
            return False
        
        else:
            res = 0
            while n > 0:
                    
                    sq = n % 10
                    res += sq*sq
                    n = n // 10

            return self.isHappy(res)
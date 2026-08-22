class Solution:
    def checkDivisibility(self, n: int) -> bool:
        text = list(map(int,str(n)))
                      
        ad = sum(text)
        pr = math.prod(text)
        res = n%(ad+pr)
        if res == 0:
            return True
        else:
            return False

        
        
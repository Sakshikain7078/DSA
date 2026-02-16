class Solution:
    def reverseBits(self, n: int) -> int:
        if n < 0:
            n = (1 << 32) + n   
        
        binary = bin(n)[2:].zfill(32)  
        reversed_binary = binary[::-1]  
        decimal = int(reversed_binary, 2)
        
        return decimal

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        l = []
        for i in s:
            l.append(int(i))
        while(len(l)>2):
            x = []
            for j in range(0,len(l)-1):
                x.append((l[j]+l[j+1])%10)
            l = x
        if l[0] == l[1]:
            return True
        return False

                
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        arr = []
        for i in str(n):
            if i != '0':
                arr.append(i)
        if not arr:
            x = 0
        else:

            x = int(''.join(arr))
        s = 0
        for d in str(x):
            s = s + int(d)
        res = x*s
        return res
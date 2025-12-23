class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = 1
        res = 0
        stk = []
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num*10+int(c)
            elif c in '-+':
                res += num*sign
                sign = -1 if c == '-' else 1
                num = 0
            elif c == '(':
                stk.append(res)
                stk.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign*num
                res *= stk.pop()
                res += stk.pop()
                num = 0
        return res+num*sign
        
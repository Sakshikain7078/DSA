class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                ans = int(stack.pop()) + int(stack.pop())
                stack.append(ans)
            elif tokens[i] == '-':
                ans = -int(stack.pop()) + int(stack.pop())
                stack.append(ans)
            elif tokens[i] == '/':
                cur = int(stack.pop())
                div = stack.pop()
                ans = int(div) // cur
                if div%cur != 0 and ans<0:
                    ans += 1
                stack.append(ans)
            elif tokens[i] == "*":
                cur = int(stack.pop())
                ans = int(stack.pop())*cur
                stack.append(ans)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
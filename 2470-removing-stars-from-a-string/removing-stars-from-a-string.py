class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for cha in s:
            if cha != "*":
                stack.append(cha)
            else:
                stack.pop()
        result = ""
        for ch in stack:
            result += ch
        return result

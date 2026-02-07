class Solution:
    def minimumDeletions(self, s: str) -> int:
        countb = 0
        deletion = 0
        for ch in s:
            if ch == 'b':
                countb += 1
            if ch == 'a':
                deletion = min(deletion+1,countb)
        return deletion
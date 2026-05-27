class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # for char in word:
        #     if char.isupper():
        #         return True
        #     else:
        #         return False
        return word.isupper() or word.islower() or word.istitle()
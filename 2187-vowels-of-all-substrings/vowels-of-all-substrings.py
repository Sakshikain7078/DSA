class Solution:
    def countVowels(self, word: str) -> int:
        vowel = set("aeiou")
        res = 0
        n = len(word)
        for i in range(n):
            if word[i] in vowel:
                res += (i+1)*(n-i)
        return res
        

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for p in "!?',;.":
            paragraph = paragraph.replace(p, ' ')
        word = paragraph.split()
        valid_word = []
        for w in word:
            if w not in banned:
                valid_word.append(w)
        freq = Counter(valid_word)
        res = max(freq, key=freq.get)
        return res

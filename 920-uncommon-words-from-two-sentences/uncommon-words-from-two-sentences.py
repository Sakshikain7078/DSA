class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        ans = s1 + " " + s2
        freq = ans.split()
        aws = Counter(freq)
        for word, count in aws.items():
            if count == 1:
                res.append(word)
        return res
       
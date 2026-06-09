class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_count = Counter()
        for char in licensePlate:
            if char.isalpha():
                license_count[char.lower()] += 1
        words.sort(key=len)
        for word in words:
            word_count = Counter(word)
            is_match = True
            for char in license_count:
                if word_count[char] < license_count[char]:
                    is_match = False
                    break
            if is_match:
                return word
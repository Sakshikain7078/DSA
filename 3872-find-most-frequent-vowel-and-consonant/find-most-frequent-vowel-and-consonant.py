class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = 'aeiou'
        vowels = 0
        consonent = 0
        list1 = []
        list2 = []
        for i in set(s):
            if i in vowel:
                list1.append(s.count(i))
            else:
                list2.append(s.count(i))
        if list1 and list2:
            return (max(list1)+max(list2))
        elif list1:
            return(max(list1))
        else:
            return max(list2)
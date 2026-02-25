class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bit_key(x):
            return (bin(x).count('1'),x)
        sorted_arr = sorted(arr,key = bit_key)
        return sorted_arr
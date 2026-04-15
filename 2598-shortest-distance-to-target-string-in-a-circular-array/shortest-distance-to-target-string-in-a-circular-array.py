class Solution:
    def closestTarget(self, words, target,startIndex):
        n = len(words)
        min_dist = float('inf')
        for i in range(n):
            if words[i] == target:
                direct_dist = abs(i-startIndex)

                circular_dist = n-direct_dist

                min_dist = min(min_dist, direct_dist, circular_dist)
        return min_dist if min_dist != float('inf') else -1
        
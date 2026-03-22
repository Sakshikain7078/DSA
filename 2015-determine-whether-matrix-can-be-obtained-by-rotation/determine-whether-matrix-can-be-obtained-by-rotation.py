from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        m = 0b1111  # all 4 rotations possible

        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:            # 0°
                    m &= 0b0111
                if mat[i][j] != target[j][n-1-i]:        # 90°
                    m &= 0b1011
                if mat[i][j] != target[n-1-i][n-1-j]:    # 180°
                    m &= 0b1101
                if mat[i][j] != target[n-1-j][i]:        # 270°
                    m &= 0b1110

                if m == 0:
                    return False

        return True
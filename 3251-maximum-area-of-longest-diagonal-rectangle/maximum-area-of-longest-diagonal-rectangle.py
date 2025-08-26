class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dim = 0
        are = 0
        for len, wid in dimensions:
            diag = sqrt(len*len + wid*wid)
            area = len*wid
            if diag > dim or (diag == dim and area > are):
                dim = diag
                are = area
        return are
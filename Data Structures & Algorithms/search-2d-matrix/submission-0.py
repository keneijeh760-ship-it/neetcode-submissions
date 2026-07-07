class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for mat in matrix:
            for val in mat:
                if target in mat:
                    return True
        return False
        
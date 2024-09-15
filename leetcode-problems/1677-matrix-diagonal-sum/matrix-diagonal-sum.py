class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_ = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i == j or i+j+1==len(mat[i]):
                    sum_ = sum_ + mat[i][j]
        return sum_
        
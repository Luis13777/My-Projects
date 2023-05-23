from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        sum = 0
        size = len(mat)

        for i in range(size):
            sum += mat[i][i]
            sum += mat[size - 1 -i][i]

        if (size%2 != 0):
            middle = size//2
            sum -= mat[middle][middle]

        return sum
  
        
        

solucao = Solution()
solucao.diagonalSum ([[1,2,3],[4,5,6],[7,8,9]])
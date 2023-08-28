class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        matrixAux = [[0] * n for i in range(n)]

        for i in range (n):
            for j in range(n):
                matrixAux[j][n-1-i] = matrix[i][j]
            
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrixAux[i][j]

        return matrix
    
print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))





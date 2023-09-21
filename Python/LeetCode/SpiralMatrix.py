class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []

        ans = []

        def Round(top, left, bottom, right):
            nonlocal ans

            if (bottom - top >= 1 and right - left >= 1):
                for i in range(left, right + 1):
                    ans.append(matrix[top][i])
                for i in range(top + 1, bottom + 1):
                    ans.append(matrix[i][right])
                for i in range(right - 1, left - 1, -1):
                    ans.append(matrix[bottom][i])
                for i in range(bottom - 1, top, -1):
                    ans.append(matrix[i][left])
            
                Round(top + 1, left + 1, bottom - 1, right -1)
            else:
                if (bottom == top):
                    for i in range(left, right + 1):
                        ans.append(matrix[top][i])
                else: 
                    for i in range(top, bottom + 1):
                        ans.append(matrix[i][right])


        Round(0,0,len(matrix) - 1, len(matrix[0])-1)

        return ans
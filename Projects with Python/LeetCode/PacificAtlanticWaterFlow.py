class Solution:
    def pacificAtlantic(self, heights):
        
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfsPacific (row, col):
            if (row, col) not in pacific:
                pacific.add((row, col))

            #baixo
            if ((row + 1 in range (rows)) and
                (heights[row + 1][col] >= heights[row][col]) and
                ((row + 1, col) not in pacific)):
                dfsPacific (row + 1, col)

            #cima
            if ((row - 1 in range (rows)) and
                (heights[row - 1][col] >= heights[row][col]) and
                ((row - 1, col) not in pacific)):
                dfsPacific (row - 1, col)

            #esquerda
            if ((col + 1 in range (cols)) and
                (heights[row][col + 1] >= heights[row][col]) and
                ((row, col + 1) not in pacific)):
                dfsPacific (row, col + 1)

            #direita
            if ((col - 1 in range (cols)) and
                (heights[row][col - 1] >= heights[row][col]) and
                ((row, col - 1) not in pacific)):
                dfsPacific (row, col - 1)


        def dfsAtlantic (row, col):
            if (row, col) not in atlantic:
                atlantic.add((row, col))

            #baixo
            if ((row + 1 in range (rows)) and
                (heights[row + 1][col] >= heights[row][col]) and
                ((row + 1, col) not in atlantic)):
                dfsAtlantic (row + 1, col)

            #cima
            if ((row - 1 in range (rows)) and
                (heights[row - 1][col] >= heights[row][col]) and
                ((row - 1, col) not in atlantic)):
                dfsAtlantic (row - 1, col)

            #esquerda
            if ((col + 1 in range (cols)) and
                (heights[row][col + 1] >= heights[row][col]) and
                ((row, col + 1) not in atlantic)):
                dfsAtlantic (row, col + 1)

            #direita
            if ((col - 1 in range (cols)) and
                (heights[row][col - 1] >= heights[row][col]) and
                ((row, col - 1) not in atlantic)):
                dfsAtlantic (row, col - 1)

        for i in range (cols):
            dfsPacific (0, i)
            dfsAtlantic (rows - 1, i)

        for i in range (rows):
            dfsPacific (i, 0)
            dfsAtlantic (i ,cols - 1)


        answer = []

        while atlantic:
            element = atlantic.pop()
            if element in pacific:

                answer.append([element[0], element[1]])

        return answer
    
solution = Solution ()
print(solution.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
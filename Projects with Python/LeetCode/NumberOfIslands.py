class Solution:
    def numIslands(self, grid) -> int:
        
        lines = len(grid)
        if (lines > 0):
            collums = len(grid[0])
        else:
            return 0

        combinations = set()
        for i in range (lines):
            for j in range (collums):
                # grid[i][j] = int(grid[i][j])
                combinations.add ((i, j))
            
        numberOfIslands = 0      

        def cleanIsland (line,collum):
            combinations.remove((line, collum))

            if ((line, collum + 1) in combinations):
                if grid[line][collum + 1] == "1":
                    cleanIsland (line, collum + 1)
                else:
                    combinations.remove((line, collum + 1))

            if ((line, collum - 1) in combinations):
                if grid[line][collum - 1] == "1":
                    cleanIsland (line, collum - 1)
                else:
                    combinations.remove((line, collum - 1))
            
            if ((line + 1, collum) in combinations):
                if grid[line + 1][collum] == "1":
                    cleanIsland (line + 1, collum)
                else:
                    combinations.remove((line + 1, collum))

            
            if ((line - 1, collum) in combinations):
                if grid[line - 1][collum] == "1":
                    cleanIsland (line - 1, collum)
                else:
                    combinations.remove((line - 1, collum))

        while (combinations):

            for i in range (lines):
                for j in range (collums):
                    if (i,j) in combinations:
                        if (grid[i][j] == "1"):
                            cleanIsland(i, j)
                            numberOfIslands += 1
                        else:
                            combinations.remove((i, j))

        return numberOfIslands

# class Solution ():
#     def numIslands(self, grid) -> int:
#         if not grid:
#             return 0
        
#         rows, cols = len(grid), len(grid[0])
#         visit = set()
#         isLands = 0

#         def bfs (r, c):
#             q = []
#             visit.add((r,c))
#             q.append((r,c))
#             while q:
#                 row, col = q[0]
#                 del(q[0])
#                 directions = [[1,0], [-1,0], [0,1], [0,-1]]
#                 for dr, dc in directions:
#                     r, c = row + dr, col + dc
#                     if (r in range(rows) and
#                         c in range(cols) and
#                         grid[r][c] == "1" and
#                         (r,c) not in visit):

#                         q.append((r,c))
#                         visit.add((r,c))


#         for r in range(rows):
#             for c in range (cols):
#                 if grid [r][c] == "1" and (r,c) not in visit:
#                     bfs(r,c)
#                     isLands += 1

#         return isLands







grid = [
  ["1","1","1","1","0"],
  ["1","0","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

solution = Solution ()

print(solution.numIslands(grid))
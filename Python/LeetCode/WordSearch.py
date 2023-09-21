class Solution:
    def exist(self, board, word):

        visited = set()
        lines = len(board)
        collums = len(board[0])

        def check (l, c, i):
            nonlocal visited
            if i == len(word) - 1 and word[i] == board[l][c]:
                return True
            if word[i] == board[l][c]:
                visited.add((l,c))

                a1 = False
                a2 = False
                a3 = False
                a4 = False

                if l - 1 in range (lines) and c in range (collums) and (l-1, c) not in visited:
                    a1 = check (l - 1, c, i+1)
                if l + 1 in range (lines) and c in range (collums) and (l+1, c) not in visited:
                    a2 = check (l + 1, c, i+1)
                if l in range (lines) and c - 1 in range (collums) and (l, c-1) not in visited:
                    a3 = check (l, c-1, i+1)
                if l in range (lines) and c + 1 in range (collums) and (l, c+1) not in visited:
                    a4 = check (l, c+1, i+1)

                if (a1 == False and a2 == False and a3 == False and a4 == False):
                    visited.remove((l,c))
                    return False
                if (a1 or a2 or a3 or a4):
                    return True
            else:
                return False


        for l in range(lines):
            for c in range(collums):
                if check (l,c,0):
                    return True

        return False
    
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))
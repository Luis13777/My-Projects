# Solution: you need to do a BFS and store the level

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        if (root == None):
            return 0
        
        level = 0
        queue = [root]

        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue[0]
                del queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1                    


        return level
    


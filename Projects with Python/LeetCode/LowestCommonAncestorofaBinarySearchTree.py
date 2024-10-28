# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def canReach (self, root, p, q):
        #BFS
        queue = [root]
        canReach = 0

        while (queue and canReach < 2):
            node = queue.pop(0)

            if node == p:
                canReach += 1
            if node == q:
                canReach += 1

            if (node.left):
                queue.append(node.left)
            if (node.right):
                queue.append(node.right)

        if canReach == 2:
            return True
        
        return False

    def lowestCommonAncestor(self, root, p, q):
        minimum = root
        maxDeepth = 0
        def DFS (node, deepth):
            nonlocal minimum
            if (deepth > maxDeepth and self.canReach(node, p, q)):
                minimum = node
                deepth = maxDeepth
            if node != p and node != q:
                if (node.left):
                    DFS (node.left, deepth + 1)
                if (node.right):
                    DFS (node.right, deepth + 1)

        DFS(root, 0)

        return minimum
    

Tree = TreeNode(6)
Tree.left = TreeNode(2)
Tree.left.left = TreeNode(0)
Tree.left.right = TreeNode(4)
Tree.left.right.left = TreeNode(3)
Tree.left.right.right = TreeNode(5)
Tree.right = TreeNode (8)
Tree.right.left = TreeNode (7)
Tree.right.right = TreeNode (9)

# print(Solution().canReach(Tree, Tree, Tree.right.right))
print(Solution().lowestCommonAncestor(Tree, Tree.left.right.left, Tree.left.right.right).val)
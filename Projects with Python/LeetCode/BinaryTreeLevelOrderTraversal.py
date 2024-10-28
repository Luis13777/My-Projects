# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):

        if root == None:
            return []

        ans = []

        #DFS
        def DFS (node, height):
            nonlocal ans
            if (len(ans) == height):
                ans.append([])
            ans[height].append(node.val)
            if node.left:
                DFS(node.left, height + 1)
            if node.right:
                DFS(node.right, height + 1)

        DFS(root, 0)
        return ans
    

Tree = TreeNode(3)
Tree.left = TreeNode(9)
Tree.right = TreeNode(20)
Tree.right.left = TreeNode(15)
Tree.right.right = TreeNode(7)

print(Solution().levelOrder(Tree))
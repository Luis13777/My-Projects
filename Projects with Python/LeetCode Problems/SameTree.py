# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:
        pStack = []
        qStack = []

        if (p != None and q == None or p == None and q != None):
            return False
        if (p == None and q == None):
            return True

        pStack.append(p)
        qStack.append(q)
        while (pStack and qStack):
            
            if (len(pStack) != len(qStack)):
                return False
            
            size = len(qStack)
            for i in range (size):
                pCur = pStack[0]
                del(pStack[0])
                qCur = qStack[0]
                del(qStack[0])

                
                if (qCur.val != pCur.val):
                    return False
                
                if (qCur.right == None and pCur.right != None):
                    return False
                
                if (qCur.right != None and pCur.right == None):
                    return False
                
                
                if (qCur.left == None and pCur.left != None):
                    return False
                
                if (qCur.left != None and pCur.left == None):
                    return False
                
                if (qCur.left != None):
                    if (qCur.left.val != pCur.left.val):
                        return False
                
                if (qCur.right != None):
                    if (qCur.right.val != pCur.right.val):
                        return False
                
                if (pCur.left != None):
                    pStack.append(pCur.left)
                if (pCur.right != None):
                    pStack.append(pCur.right)
                if (qCur.left != None):
                    qStack.append(qCur.left)
                if (qCur.right != None):
                    qStack.append(qCur.right)
        
        return True


# do a BFS on both trees and compare to see weather they are the same


solution = Solution ()

p = TreeNode(1)
# p.left = TreeNode (2)
p.right = TreeNode (2)

q = TreeNode(1)
q.left = TreeNode (2)
# q.right = TreeNode (3)

print(solution.isSameTree(p, q))
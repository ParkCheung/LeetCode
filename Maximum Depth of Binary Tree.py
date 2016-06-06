# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#递归分别计算左子树和右子树的深度 DFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
#debug
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

s = Solution()
print(s.maxDepth(root))

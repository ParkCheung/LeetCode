# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.left is None or root.right is None:
            return root

        if self.cover(root.left, p) and self.cover(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)

        if self.cover(root.right, p) and self.cover(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)

        return root

    def cover(self, root, n):
        if root is None:
            return False
        if root is n:
            return True

        return self.cover(root.left, n) or self.cover(root.right, n)

# debug
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.left = TreeNode(6)
# debug
s = Solution()
print(s.lowestCommonAncestor(root, root.left.left, root.left).val)

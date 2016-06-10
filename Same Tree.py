# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 1 如果两个节点都为空，则相等。
        # 2 如果仅有一个节点为空，则不等。
        # 3 如果节点的值相等，并且左子树和右子树分别相等，则返回相等，否则返回不等。

        if p == None and q == None:
            return True
        elif p != None and q != None and p.val == q.val:
            pass
        else:
            return False

        # 先比较左子树 如果False 直接返回不再比较右子树
        if not self.isSameTree(p.left, q.left):
            return False
        # 再比较右子树
        return self.isSameTree(p.right, q.right)


# debug
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(4)

s = Solution()
print(s.isSameTree(root, root1))

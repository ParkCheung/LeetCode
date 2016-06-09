# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # 1. 1->2->4->4->None
        node.val = node.next.val

        # 2. 1->2->4->None
        node.next = node.next.next

        return node


def printNode(node):
    while node != None:
        if node.next == None:
            print(node.val)
        else:
            print(node.val, end='->')
        node = node.next

# debug
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

printNode(node1)

s = Solution()
s.deleteNode(node4)

printNode(node1)

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res

def printNode(node):
    while node != None:
        if node.next == None:
            print(node.val)
            break
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
printNode(s.reverseList(node1))

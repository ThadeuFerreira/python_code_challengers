from typing import List
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            root = list1
            list1 = list1.next
        else:
            root = list2
            list2 = list2.next
        node = root
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        if list1 is None:
            node.next = list2
        else:
            node.next = list1
        return root
    
    def printList(self, node):
        while node is not None:
            print(node.val)
            node = node.next

s = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

s.printList(list1)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
list2.next.next.next = ListNode(5)
list2.next.next.next.next = ListNode(6)
s.printList(list2)

node = s.mergeTwoLists(list1, list2)
s.printList(node)
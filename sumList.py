from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        al1 = []
        node = l1
        while node:
            al1.append(node.val)
            node = node.next
        al2 = []
        node = l2
        while node:
            al2.append(node.val)
            node = node.next
            
        #reverse al1 and al2
        al1.reverse()
        al2.reverse()
        
        carry = 0
        index = 0
        result = []
        while index < len(al1) and index < len(al2):
            s = al1[index] + al2[index] + carry
            result.append(s%10)
            carry = s // 10
            index += 1
            
        while index < len(al1):
            s = al1[index] + carry
            result.append(s%10)
            carry = s // 10
            index += 1
            
        while index < len(al2):
            s = al2[index] + carry
            result.append(s%10)
            carry = s // 10
            index += 1
        if carry > 0:
            result.append(carry)
        result.reverse()
        node = ListNode(result[0])
        head = node
        for i in range(1, len(result)):
            node.next = ListNode(result[i])
            node = node.next
        return head

s = Solution()
l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
l2 = ListNode(5, ListNode(6, ListNode(4)))   

print(s.addTwoNumbers(l1, l2))
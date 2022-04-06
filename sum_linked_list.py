from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def listToNumber(node):
        number = 0
        decimal = 0
        while node is not None:
            number += (10**decimal)*node.val
            node = node.next
            decimal+=1
        return number
    
    def numberToList(number):
        root = ListNode(number%10)
        number = number // 10
        node = root
        while number > 0:
            node.next = ListNode(number%10)
            number = number//10
            node = node.next
        return root               
            
    
    n1 = listToNumber(l1) 
    n2 = listToNumber(l2)
    number = n1 + n2
    return numberToList(number)

def printList(node):
    while node is not None:
        print(node.val)
        node = node.next

root1 = ListNode(2)
root1.next = ListNode(4)
root1.next.next = ListNode(3)

root2 = ListNode(5)
root2.next = ListNode(6)
root2.next.next = ListNode(4)

r = addTwoNumbers(root1, root2)
printList(r)
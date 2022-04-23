class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def addleft(self, data):
        new_node = DNode(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def addright(self, data):
        new_node = DNode(data)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    def popleft(self):
        if self.head == None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data
    def popright(self):
        if self.tail == None:
            return None
        else:
            data = self.tail.data
            self.tail = self.tail.prev
            self.size -= 1
            return data
    def getAt(self, index):
        if index < 0 or index >= self.size:
            return None
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            return curr.data
    def insertAt(self, index, data):
        if index < 0 or index > self.size:
            return False
        else:
            new_node = DNode(data)
            if index == 0:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif index == self.size:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                curr = self.head
                for i in range(index):
                    curr = curr.next
                new_node.next = curr
                new_node.prev = curr.prev
                curr.prev.next = new_node
                curr.prev = new_node
            self.size += 1
            return True
    def removeAt(self, index):
        if index < 0 or index >= self.size:
            return False
        else:
            if index == 0:
                self.head = self.head.next
                self.head.prev = None
            elif index == self.size - 1:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                curr = self.head
                for i in range(index):
                    curr = curr.next
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
            self.size -= 1
            return True
    def reverse(self):
        new_list = DLinkedList()
        curr = self.tail
        while curr != None:
            new_list.addright(curr.data)
            curr = curr.prev
        return new_list
        

    def slice(self, start, end):
        if start < 0 or start >= self.size or end < 0 or end >= self.size:
            return None
        else:
            if start > end:
                start, end = end, start
            new_list = DLinkedList()
            curr = self.head
            for i in range(start):
                curr = curr.next
            for i in range(end - start + 1):
                new_list.addleft(curr.data)
                curr = curr.next
            return new_list
    def printlist(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next

#Add up to N Max integer elements
# has function popMax()
# has function popMin() 
class MaxHeap:
    # Constructor to initialize a Max Heap
    # heap is a double linked list add in order from left to right, from min to max
    # MaxHeap has a limited capacity, if new element is larger than the smallest element in the heap, remove the smallest element and add the new element in order
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.heap = DLinkedList()
    def add(self, data):
        if self.size == self.capacity:
            if data > self.heap.getAt(0):
                self.heap.popleft()
                self.heap.addright(data)
        else:
            self.heap.addleft(data)
            self.size += 1
    def peekMax(self):
        if self.size == 0:
            return None
        else:
            return self.heap.getAt(0)
    def peekMin(self):
        if self.size == 0:
            return None
        else:
            return self.heap.getAt(self.size - 1)

    

    



dl = DLinkedList()
dl.addright(1)
dl.addright(2)
dl.addright(3)
dl.addright(4)
dl.printlist()
dr = dl.reverse()
print('-'*20)
dr.printlist()
class ListNode:
    def __init__(self,data,next_node = None,previous_node = None) -> None:
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node
    
class SingllyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def insert(self,data):
        if not self.head:
            self.head = self.tail = ListNode(data)
        self.tail.next_node=ListNode(data)
        self.tail=self.tail.next_node
    def delete(self,data):
        if not self.head:
            return -1
        temp = self.head
        prev = None
        while temp and temp.data!=data:
            prev = temp
            temp = temp.next_node
        if not temp:
            return -1
        prev.next_node = temp.next_node
    
class DoubblyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def insert(self,data):
        if not self.head:
            self.head=self.tail=ListNode(data)
        
        new_node = ListNode(data)
        self.tail.next_node = new_node
        new_node.previous_node=self.tail
        self.tail = self.tail.next_node

    #returns type of delete happening
    def delete(self,data):
        if not self.head:
            return -1
        
        temp = self.head
        while temp and temp.data != data:
            temp=temp.next_node
        if temp == self.head:
            self.head = self.head.next_node
            return 1
        if temp == self.tail:
            self.tail=self.tail.previous_node
            return 1
        temp.previous_node.next_node = temp.next_node
        temp.next_node.previous_node = temp.previous_node
        return 0
    
class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    

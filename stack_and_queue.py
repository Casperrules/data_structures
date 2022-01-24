class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.previous = None
    
class Stack:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    def push(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        self.head.next = new_node
        new_node.previous = self.head
        self.head=self.head.next
        self.size+=1

    def pop(self):
        if self.size == 0:
            raise Exception('Empty stack. Nothing to pop')
        popped_val = self.head.data
        self.head = self.head.previous
        if self.head:
            self.head.next = None
        self.size-=1
        return popped_val
    
    def peek(self):
        return self.head.data

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    
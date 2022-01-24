class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.previous = None
# a deque will need to be implemented using a DLL so have that option with this nodde. <Future Thinkings>
    
class Stack:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    def push(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.size+=1
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
    
    def enqueue(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            self.size+=1
            return
        self.tail.next = new_node
        self.tail = self.tail.next
        self.size+=1
    
    def dequeue(self):
        if self.size==0:
            raise Exception('Empty queue can not be dequeued')
        deququed_val = self.head.data
        self.head = self.head.next
        self.size-=1
        if self.size==0:
            self.tail = self.head = None
        return deququed_val
    
    def peek(self):
        return self.head.data



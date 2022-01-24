class MinHeap:
    def __init__(self,arr=[]) -> None:
        self.heap = arr
        n = self.size()-1
        for i in range(n//2,-1,-1):
            self.heapify(i)
    
    def size(self):
        return len(self.heap)

    def heapify(self,index):
        smallest = index
        left_child = 2*index+1
        right_child = 2*index+2
        if left_child<self.size() and self.heap[smallest]>self.heap[left_child]:
            smallest = left_child
        if right_child<self.size() and self.heap[smallest]>self.heap[right_child]:
            smallest = right_child
        if smallest != index:
            self.heap[index],self.heap[smallest] = self.heap[smallest],self.heap[index]
            self.heapify(smallest)

    def insert(self,data):
        self.heap.append(data)
        new_child_index = self.size()-1
        parent = (new_child_index)//2
        while self.heap[parent]>self.heap[new_child_index]:
            self.heap[new_child_index],self.heap[parent] = self.heap[parent],self.heap[new_child_index]
            new_child_index = parent
            parent = (new_child_index)//2
        
    # delete root
    def get_min(self):
        if self.size()==0:
            raise Exception('heap is empty')
        self.heap[-1],self.heap[0] = self.heap[0],self.heap[-1]
        min_val = self.heap.pop(-1)
        #heapify logic on root
        self.heapify(0)
        return min_val

    def peek(self):
        if self.size()>0:
            return self.heap[0]
        else:
            raise Exception('heap is empty')
            
class MaxHeap:
    def __init__(self,arr=[]) -> None:
        self.heap = arr
        if not self.heap:
            return
        for i in range((self.size()-1)//2,-1,-1):
            self.heapify(i)
    
    def size(self):
        return len(self.heap)
    
    def heapify(self,index):
        largest = index
        left_child = 2*index+1
        right_child = 2*index+2
        if left_child < self.size() and self.heap[left_child]>self.heap[largest]:
            largest = left_child
        if right_child<self.size() and self.heap[right_child]>self.heap[largest]:
            largest = right_child
        if largest!=index:
            self.heap[largest],self.heap[index] = self.heap[index],self.heap[largest]
            self.heapify(largest)

    def insert(self,data):
        self.heap.append(data)
        new_node_index = self.size()-1
        parent_index = new_node_index//2
        while self.heap[new_node_index]>self.heap[parent_index]:
            self.heap[new_node_index],self.heap[parent_index] = \
                self.heap[parent_index],self.heap[new_node_index]
            new_node_index = parent_index
            parent_index = new_node_index//2
    
    def get_max(self):
        if self.size()==0:
            raise Exception('Heap is empty. can not get max element from empty heap')
        self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]
        max_val = self.heap.pop()
        self.heapify(0)
        return max_val
    
    def peek(self):
        if self.size()==0:
            raise Exception('heap is empty. no max element found')
        return self.heap[0]
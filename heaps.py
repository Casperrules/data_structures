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
            


## Testing Min heap
# my_min_heap = MinHeap([10,5,1,4,2,3,8,7,0,6,9])
# my_min_heap.min_heapify()
# arr = [i for i in range(100_000_000,-1,-1)] #for very big input, it is a little<very> slow
# print("done")
# my_min_heap = MinHeap(arr)
# my_min_heap.min_heapify()
# print(my_min_heap.min_heap[0])


class MaxHeap:
    def __init__(self,arr=[]) -> None:
        self.heap = arr
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
my_max_heap = MaxHeap([10,5,1,4,2,3,8,7,0,6,9])
print(my_max_heap.heap)
my_min_heap = MinHeap([10,5,1,4,2,3,8,7,0,6,9])
print(my_min_heap.heap)
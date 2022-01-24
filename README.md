# data_structures
python implementation of some commonly used data structures
## Data Structures Implemented:
### Binary Search Tree:
* a BST is a tree data structure which, at any node has all values to the left smaller than self and all values to the right greater.
* in BST, insertion, search and deletion are all O(H) operation where, H is height of the tree.
* norder traversal of a BST returns values in sorted order.
* [link to BST implementation code](https://github.com/Casperrules/data_structures/blob/master/binary_search_tree.py)

---
### Linked List:
* linked lists are linear data structures
* following are the lists implemented in the code: 1) Sigally Linked List. 2) Doubally Linked List. 3) Circular Doubally Linked List.
* singally linked list moves only forward(good for queue implementation), doubally linked list can more forward and back(good for stack implementation).
* [Link to Linked lists implementation](https://github.com/Casperrules/data_structures/blob/master/linked_lists.py)

---
### Heaps:
* heaps are complete binary trees(i.e. each level is filled except the last one and filled from left to right)
* heaps are good if you want to obtain max or min element(based on any criteria) in O(1) time
* they can be implemented using an array
* the array can be seen as a serialized heap tree. a heap tree can be created from it using level order traversal and filling values
* heaps are easy and cool
* [Link to heaps implementation](https://github.com/Casperrules/data_structures/blob/master/heaps.py)

---
### Stacks and Queues:
* another liner data structure(I mean both of them are linear)
* stack is a `First In Last Out` data structure.. i.e. the last element inserted to a stack is first one to be removed
* I use a Doublly Linked List for the implementation for stacks, using the head of the list to keep track of "last in"
* Queues are a `First In First Out` data structure i.e. the first element inerted is the first one removed(like in a real queue<which I know is obvious from the name but well, my README, my Rules :)>)
* I use Singally Linked List logic to implement the queue as it dodes not reaquire back movement
* clircular queue can be implemented using a Circular Singally Linked List
* [Link to Stack and Queue Implementation](https://github.com/Casperrules/data_structures/blob/master/stack_and_queue.py)


---- More Implementations Coming Soon(files are already created for them) ----

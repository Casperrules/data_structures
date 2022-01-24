class TreeNode:
    def __init__(self,data=None,left=None,right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
    
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    #assuming if repetetion, completely ignore insertion
    def insert(self,data):
        if not self.root:
            self.root = TreeNode(data)
            return
        curr = self.root
        while True:
            if curr.data == data:
                return
            elif curr.data>data:
                if not curr.left:
                    curr.left = TreeNode(data)
                    return
                else:
                    curr = curr.left
            elif curr.data<data:
                if not curr.right:
                    curr.right = TreeNode(data)
                    return
                else:
                    curr = curr.right
        #O(H) time O(1) space

    def search(self,data):
        curr = self.root
        while True:
            if curr.data == data:
                return curr
            elif curr.data<data:
                curr = curr.right
            elif curr.data>data:
                curr = curr.left
            if not curr:
                return TreeNode(-1)
    
    def delete(self,data):
        def delete_helper(root,data):
            if not root:
                return
            left = delete_helper(root.left,data)
            right = delete_helper(root.right,data)
            if root.data == data:
                if not root.left and not root.right:
                    return
                if not root.right:
                    return root.left

                if not root.left:
                    return root.right

                curr = root.right
                while curr.left:
                    curr = curr.left
                root.data = curr.data
                delete_helper(root.right,curr.data)
            root.left = left
            root.right = right
            return root

        self.root = delete_helper(self.root,data)


    def inorder(self):
        def helper(root):
            if root:
                helper(root.left)
                print(root.data)
                helper(root.right)
        helper(self.root)
    def inorder_iterative(self):
        stack = [self.root]
        curr = self.root.left
        while curr or stack:
            if curr:
                stack.append(curr)
                curr=curr.left
            else:
                curr=stack.pop(-1)
                print(curr.data)
                curr = curr.right
                

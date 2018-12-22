# implementation of a binary search tree

class Node(object):
    
    def __init__(self, data):
        self.key = data
        self.left_child = None
        self.right_child = None
        
        
class binary_search_tree(object):
    
    def __init__(self):
        self.root = None
    
    # helper function for insert_node    
    def insert(self, data):
        
        new_node = Node(data)
        
        if self.root == None:
            self.root = new_node
        else:
            self.insert_node(data, self.root)
    
    # O(LogN) if the tree is balanced 
    def insert_node(self, data, root):
        new_node = Node(data)
        
        if new_node.key > root.key:
            if root.right_child is None:
                root.right_child = new_node
            else:
                self.insert_node(data, root.right_child)
        else:
            if root.left_child is None:
                root.left_child = new_node
            else:
                self.insert_node(data, root.left_child)
    
    # helper get_min            
    def get_min_helper(self):      
        if self.root is None:
            return -1
        else:
            return self.get_min(self.root)
    
    #O(LogN)
    def get_min(self, node):
        
        if node.left_child:
            self.get_min(node.left_child)
        
        return node.key
    
    def get_max_helper(self):
        if self.root:
            return self.get_max(self.root)
        else:
            return -1
    
    def get_max(self, node):
        
        if node.right_child:
            get_max(node.right_child)
        
        return node.key
    
    def treverse(self):
        if self.root:
            self.treverse_in_order(self, self.root)
        
    def treverse_in_order(self, node):
        
        if node.left_child:
            self.treverse_in_order(node.left_child)
            
        print(node.key)
        
        if node.right_child:
            self.treverse_in_order(node.right_child)
        

def main():
    
    bst = binary_search_tree()
    bst.insert(5)
    bst.insert(8)
    bst.insert(3)
    bst.insert(13)
    bst.treverse()

main()
            
            
            
            
            
    
    


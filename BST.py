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
                
    def remove(self, data):
        if self.root:
            self.root = self.remove_node(data, self.root)
      
    # Remove node    
    def remove_node(self, data, node):
        
        if node is None:
            return None
        
        if node.key > data:
            node.left_child = self.remove_node(data, node.left_child)
            
        elif node.key < data:
            node.right_child = self.remove_node(data, node.right_child)
            
        else:
            # If leaf node
            if not node.right_child and not node.left_child:
                print("Removing leaf node")
                del node
                return None
            
            # if no right child
            elif not node.right_child:
                print("Removing root node with no right child")
                temp = node.left_child
                del node
                return temp
            
            # if not left child
            elif not node.left_child:
                print("Removing root node with no left child")
                temp = node.right_child
                del node
                return temp
            
            # if contains left and right child 
            else: 
                print("Removing root node")
                pred = self.get_pred(node.left_child)
                node.key = pred.key
                node.left_child = self.remove_node(pred.key, node.left_child)
                
        return node
    
    
    # Get the predecessor of the node to delete
    def get_pred(self, node):
        
        if node.right_child:
            return self.get_pred(node.right_child)
        
        return node
            
   
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
    
    #Helper for get_max
    def get_max_helper(self):
        if self.root:
            return self.get_max(self.root)
        else:
            return -1
        
    #O(LogN)
    def get_max(self, node):
        
        if node.right_child:
            get_max(node.right_child)
        
        return node.key
    
    def treverse(self):
        if self.root:
            self.treverse_in_order(self.root)
        
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
    bst.insert(6)
    bst.insert(7)
    bst.insert(10)
    bst.insert(11)
    bst.insert(13)
    bst.remove(8)
    bst.treverse() # Output: 5, 6, 7, 10, 11, 13

main()
            
            
            
            
            
    
    


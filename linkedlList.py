# -*- coding: utf-8 -*-

class Node(object):
    
    def __init__(self, data):
        self.key = data
        self.next = None
        
class Linkedlist(object):
    
    def __init__(self):
        self.head = None;
        self.size = 0;     # To keep track of size
    
    # O(1)
    def insert_start(self, data):
        newNode = Node(data)
        self.size = self.size + 1
        
        if (self.head is None):
            self.head = newNode
            
        else:
            newNode.next = self.head
            self.head = newNode
    
    # O(N)        
    def insert_end(self, data):
        
        actual_node = self.head
        self.size = self.size + 1
        
        while actual_node.next is not None:
            actual_node = actual_node.next
            
        newNode = Node(data)
        actual_node.next = newNode
        
    #Delete node
    def delete_node(self, data):
        
        if self.head is None:
            return
            
        current_node = self.head
        previous_node = None
        
        while(current_node.key is not data and current_node is not None):
            previous_node = current_node
            current_node = current_node.next

        # If delete Node does not exist 
        if current_node is None:
            return
        
        self.size = self.size - 1
        
        # is delete node is head
        if previous_node is None:
            self.head = current_node.next
            
        previous_node.next = current_node.next
    
    # get length of linkedList, O(1)
    def length(self):
        return self.size
    
    #traverse the linkedlist to get length, O(N)
    def length2(self):
        temp = self.head
        count = 0
        
        while temp.next is not None:
            count += 1
            temp = temp.next
        
        return count
    
    #print linkedList
    def traverse_linked_list(self):
        actual_node = self.head
        
        while actual_node is not None:
            print(actual_node.key)
            actual_node = actual_node.next
            
def main():
    
    linkedlist = Linkedlist()
    linkedlist.insert_start(32)
    linkedlist.insert_start(12)
    linkedlist.insert_start(3)
    linkedlist.insert_end(122)
    
    linkedlist.traverse_linked_list() # 3, 12, 32, 122
    
            
main()
    
    
# Stack data structure implementation with arrays

class Stack(object):
    
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return self.stack == []            
    
    # O(1)
    def push(self, data):
        self.stack.append(data)
    # O(1)
    def pop(self):
        data = self.stack[-1]
        self.stack.pop()
        return data
    
    def peak(self):
        return self.stack[-1]
    #O(1)
    def size_stack(self):
        return len(self.stack)
    
def main():
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.size_stack()) # 3
    print(stack.peak()        # 3
    print(stack.pop())        # 3
    print(stack.pop())        # 2
    
main()
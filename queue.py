#Queue implementation with array

class Queue(object):
    
    def __init__(self):
        self.queue = []
    # O(1)
    def enqueue(self,data):
        self.queue.append(data)
    
    def is_empty(self):
        return self.queue == []
    # O(1)
    def dequeue(self):
        return self.queue.pop(0)
    # O(1)
    def size_of_queue(self):
        return len(self.queue)
    
    def peak(self):
        return self.queue[0]
    

def main():
    queue = Queue()
    
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(3)
    print(queue.size_of_queue())  #3
    print(queue.peak())           #5
    print(queue.dequeue())        #5
    
main()
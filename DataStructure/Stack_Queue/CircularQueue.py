class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = 0
        self.max_size = k
        self.data = [None]*k
        self.front = self.rear = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size == self.max_size: # isfull
            return False
        self.rear = (self.rear + 1) % self.max_size
        self.data[self.rear] = value
        self.size += 1
        if self.front == -1: # size 0 -> 1
            self.front = self.rear
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size == 0: # isEmpty
            return False
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        if self.size == 0:
            self.front = self.rear = -1
        return True
        
    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.size == 0:
            return -1
        return self.data[self.front]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.size == 0:
            return -1
        return self.data[self.rear]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == self.max_size
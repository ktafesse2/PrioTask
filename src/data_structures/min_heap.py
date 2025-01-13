class MinHeap:
    ### Capacity is max amount of elements to be stored within the heap
    def __init__(self, capacity): 
        # Place to store data using array
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    ### Helper methods to calculate parent and child indices
    ### And to check existence of nodes
    ### Parent =  i - 1)//2
    ### left =    2 * i + 1
    ### right =   2 * i + 2

    def getParentIndex(self, index):
        return (index -1) // 2
    def getLeftChildIndex(self, index):
        return 2 * index + 1
    def getRightChildIndex(self, index):
        return 2 * index + 2
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    ### Helper methods to get data from actual nodes
    def parent(self, index):
        return self.storage[self.getParentIndex(index)]
    def leftChild(self, index) :
        return self.storage[self.getLeftChildIndex(index)]
    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]
    
    ### Other helper Methods
    def isFull(self):
        return self.size == self.capacity
    def isEmpty(self):
        return self.size == 0
    def swap(self, index1, index2):
        tmp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = tmp

    ### Inserting into heap
    def insert(self, data):
        if (self.isFull()):
            raise ValueError ("Heap is Full")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp(index=self.size-1)
    ### Heapify method to make sure heap is in correct order after insertion
    def heapifyUp(self, index):
        while(self.hasParent(index) and
              self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)
    
    ### Return minimum value without deleting
    def getMin(self):
        return self.storage[0]
    ###  Return minimum value and delete it
    def removeMin(self):
        if(self.isEmpty()):
            raise ValueError("Empty Heap")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)
        return data
    ### Heapify method to make sure heap is in correct order after deletion
    def heapifyDown(self, index):
        # check if left child (heap must have left child to have right child)
        while(self.hasLeftChild(index)):

            # Get the smaller node between right and left child
            smaller = self.getLeftChildIndex(index)
            if(self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                smaller = self.getRightChildIndex(index)

            # Check if current node is already smaller than smallest of its two children
            if (self.storage[index] < self.storage[smaller]):
                break

            # If not swap nodes and continue
            else:
                self.swap(index, smaller)
                index = smaller

    # Update an existing node with a new value
    def update(self, index, new):
        if index > self.size -1 or index < 0:
            raise ValueError("Index not recognized")
        old = self.storage[index]
        self.storage[index] = new
        if new > old:
            self.heapifyDown(index=index)
        elif new < old:
            self.heapifyUp(index=index)   
    # Delete an existing node
    def delete(self, index):
        if(self.isEmpty()):
            raise ValueError("Empty Heap")
        self.storage[index] = self.storage[self.size - 1]
        self.size -= 1
        if self.hasParent(index) and self.storage[index] < self.storage[self.getParentIndex(index)]:
            self.heapifyUp(index=index)
        else:
            self.heapifyDown(index=index)
    
    ### Build heap from an array
    def buildHeap(self, arr):
        if len(arr) > self.capacity:
            raise ValueError("Array Size larger than Capacity")
        if self.size + len(arr) > self.capacity:
            raise ValueError("Adding Array will put heap over capacity")
        
        for i in range(len(arr)):
            self.storage[i] = arr[i]

        self.size += len(arr)

        start_idx = (self.size // 2) - 1
        for i in range(start_idx, -1, -1):
            self.heapifyDown(i)
    ### Reset heap
    def reset(self):
        for i in range(self.size):
            self.storage[i] = 0
            self.size -= 1      
    ### Print contents of heap
    def print_heap(self):
        print(self.storage[:self.size])
import numpy as np

# Create BinaryMinHeap Class-----------------------------------------------------------
class BinaryMinHeap(object):
    
# Create initial properties of the heap
    def __init__(self, size):
        self.size = size  ## Set Heap Size Limit
        self.heapSize = 0 ## Count UP for Heap Index
        self.data = [0] * size
        
#--- Define each node of the heap
    def Node(self, value):
        self.value = value
        return self.value
        
#--- Run index search through heap
    def getleftChildIndex(self, i): return (2 * i + 1)
    def getRightChildIndex(self, i): return (2 * i  + 2)
    def getParentIndex(self, i): return int((i - 1) / 2)
    def isEmpty(self): return self.heapSize == 0
    
#--- Check heap size
    def getMin(self):
        if self.isEmpty(): 
            self.ex.HeapException(self, 'Storage is Empty!')
            return
        else: return self.data[0]
    
#--- Insert New Node
    def insert(self, value):
        # Check if heap is full
        if self.heapSize == self.size:
            self.ex.HeapException(self, 'Storage is full!')
            return
        else:
            self.data[self.heapSize] = self.Node(value)
            print('[{0}]: {1}'.format(self.heapSize,
                                          self.data[self.heapSize]))
            self.indexUp(self.heapSize)
            self.heapSize += 1
                
#--- Remove smallest node from the heap
    def removeMin(self):
        if self.getMin():
            self.data[0] = self.data[self.heapSize - 1]
            self.data[-1] = None
            self.heapSize -= 1
            if self.heapSize > 0:
                self.indexDown(0)
    
#--- Reindex Heap When Node Has Been Added
    def indexUp(self, i):
        tmp = 0
        if i > 0:
            pi = self.getParentIndex(i)
            if self.data[pi] > self.data[i]:
                tmp = self.data[pi]
                self.data[pi] = self.data[i]
                self.data[i] = tmp
                self.indexUp(pi)

#--- Reindex Heap When Node Has Been Removed
    def indexDown(self, i):
        li = 0
        ri = 0
        mi = 0
        tmp = 0
        li = self.getleftChildIndex(i)
        ri = self.getRightChildIndex(i)
        if ri >= self.heapSize:
            if li >= self.heapSize: return
            else: mi = li
        else:
            if self.data[li] <= self.data[ri]: mi = li
            else: mi = ri
        if self.data[i] > self.data[mi]:
            tmp = self.data[mi]
            self.data[mi] = self.data[i]
            self.data[i] = tmp
            self.indexDown(mi)
            
#--- Function to display display data
    def line(self):
        print('-------------------------------------------')

    def show(self): 
        self.line()
        print('Heap Size: [{0} / {1}]'.format(self.heapSize, 
                                              self.size))
        self.line()
        heapIndex = []
        for i in range(0, self.heapSize):
            heapIndex.append(i)
            print('[{0}]: {1}'.format(heapIndex[i],
                                      self.data[i]))
        self.line()
        print()
        
#---Create HeapException Class------------------------------------------------------
    class ex(Exception):
        def __init__(self, e):
            self.e = e

        def __str__(self):
            return repr(self.e)

        def HeapException(self, e):
            print('HeapException: {0}'.format(e))
                
#-----End HeapException Class-------------------------------------------------------

    def BinaryMinHeap(self, size):
        self.heapSize = 0
        self.data = []
        
#---End BinMinHeap Class------------------------------------------------------------
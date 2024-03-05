# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        
        parentIdx =(len(array)-1)//2
        for current in reversed(range(parentIdx+1)):
            self.siftDown (current,len(array)-1,array)
        return array    
        
    def siftDown(self, current, endIdx, heap):
         childOne = current * 2 + 1
         while childOne <= endIdx:
             childTwo = current * 2 + 2 if current * 2 + 2 <= endIdx else -1
             if childTwo != -1 and heap[childTwo] < heap[childOne]:
                 idxSwap = childTwo  # Swap with the smaller child
             else:
                 idxSwap = childOne
             if heap[idxSwap] < heap[current]:
                 self.swap(current, idxSwap, heap)
                 current = idxSwap
                 childOne = current * 2 + 1
             else:
                 break
             
                    

    def siftUp(self, currentIdx, heap):
            parentIdx = (currentIdx - 1) // 2
            while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
                self.swap(currentIdx, parentIdx, heap)
                currentIdx = parentIdx
                parentIdx = (currentIdx - 1) // 2


    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        self.swap(0,len(self.heap)-1,self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0,len(self.heap)-1,self.heap)
        
        return valueToRemove

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap)-1,self.heap)
    def swap(self,i,j,heap):
        heap[i],heap[j]=heap[j],heap[i]
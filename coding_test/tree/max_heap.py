class Heap:
    def __init__(self, arr):
        self.heapify(arr)
    
    def heapify(arr):
        

class Node:
    def __init__(self,key,parent=None,left=None,right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def search(self, k):
        if self.key == k or self is None:
            return self
        if self.key <= k:
            return self.left.search(k)
        return self.right.search(k)
        
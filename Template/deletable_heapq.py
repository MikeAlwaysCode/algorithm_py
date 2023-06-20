from heapq import *


class deletable_heapq:
    def __init__(self, initial = []):
        if initial:
            self.q = initial
            heapify(self.q)
        else: self.q = []
        self.q_del = []
 
    def propagate(self):
        while self.q_del and self.q[0] == self.q_del[0]:
            heappop(self.q)
            heappop(self.q_del)
 
    def heappop(self):
        self.propagate()
        return heappop(self.q)
    
    def __len__(self):
        return len(self.q) - len(self.q_del)        
 
    def top(self):
        self.propagate()
        return self.q[0]
            
    def remove(self,x):
        heappush(self.q_del,x)
 
    def heappush(self,x):
        heappush(self.q,x)
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
 
class SumOfTopK:
    def __init__(self, K, initial = []):
        #assert len(initial) <= K
        self.K = K
        self.val = sum(initial)
        initial.sort()
        self.q_topK = deletable_heapq(initial[:K])
        self.q_other = deletable_heapq(initial[K:])
 
    def get(self):
        return self.val
    
    def add(self,v):
        self.q_topK.heappush(v)
        self.val += v
        if len(self.q_topK) == self.K+1:
            x = self.q_topK.heappop()
            self.val -= x
            self.q_other.heappush(-x)
 
    def remove(self,v):
        t = self.q_topK.top()
        if t <= v:
            self.q_topK.remove(v)
            self.val -= v
            if len(self.q_other):
                x = -self.q_other.heappop()
                self.val += x
                self.q_topK.heappush(x)
        else:
            self.q_other.remove(-v)
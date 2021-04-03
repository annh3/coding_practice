import heapq

"""
def heapsort2(iterable):
    h = []
    heapq._heapify_max(h)
    for value in iterable:
        _heappush_max(h, value)
    return [_heappop_max(h) for i in range(len(h))]
"""

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []
        self.hi = []
        

    def addNum(self, num: int) -> None:
        # edge / base cases
        if len(self.lo) == 0:
            self.lo.append(num)
            # print("apples")
            return
        
        # where does this number fall?
        if num <= self.lo[0]:
            # print("num: ", num, " is less than ", self.lo[-1] )
            if len(self.lo) > len(self.hi):
                tmp = self.lo.pop(0)
                self.hi.append(tmp)
                heapq.heapify(self.hi)
                
            self.lo.append(num)
            heapq._heapify_max(self.lo)
            # print("lo after heapify: ", self.lo)
                
        else:
            self.hi.append(num)
            heapq.heapify(self.hi)
            if len(self.hi) > len(self.lo):
                tmp = self.hi.pop(0)
                self.lo.append(tmp)
                heapq._heapify_max(self.lo)
        # print("self.lo: ", self.lo)
        # print("self.hi: ", self.hi)
        
        

    def findMedian(self) -> float:
        #print("finding median")
        if len(self.lo) == len(self.hi):
            # calc
            return (self.lo[0] + self.hi[0]) / 2
        else:
            return self.lo[0] # python heap is min heap by default

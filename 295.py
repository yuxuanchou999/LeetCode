class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__maxheap = []
        self.__minheap = []
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.__maxheap, -num)
        heapq.heappush(self.__minheap, -heapq.heappop(self.__maxheap))
        if len(self.__maxheap) < len(self.__minheap):
            heapq.heappush(self.__maxheap, -heapq.heappop(self.__minheap))
               

    def findMedian(self):
        """
        :rtype: float
        """
        return -1.0 * self.__maxheap[0] if len(self.__minheap) < len(self.__maxheap) else\
    (self.__minheap[0] - self.__maxheap[0]) * 0.5
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

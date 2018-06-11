class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly_num = 0
        a = []
        heapq.heappush(a, 1)
        for _ in range(n):
            ugly_num = heapq.heappop(a)
            if ugly_num % 2 == 0:
                heapq.heappush(a, ugly_num * 2)
            elif ugly_num % 3 == 0:
                heapq.heappush(a, ugly_num * 2)
                heapq.heappush(a, ugly_num * 3)
            else:
                heapq.heappush(a, ugly_num * 2)
                heapq.heappush(a, ugly_num * 3)
                heapq.heappush(a, ugly_num * 5)
        return ugly_num
                

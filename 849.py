class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        ans, st = 0, -1
        for i in range(len(seats)):
            if seats[i] == 1:
                if st == -1:
                    ans = max(ans, i)
                else:
                    ans = max(ans, (i - st) // 2)
                st = i
            else:
                if i == len(seats) - 1:
                    ans = max(ans, i - st)
        return ans
                

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res, l, stk = [0] * len(temperatures), len(temperatures), []
        for i in range(l):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                idx = stk.pop()
                res[idx] = i - idx
            stk.append(i)
        return res
        

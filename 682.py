class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans, dp = 0, []
        for i in range(len(ops)):
                
            if ops[i] == '+':
                dp.append(int(dp[-1]) + int(dp[-2]))
                ans += dp[-1]
            elif ops[i] == 'C':
                ans -= dp[-1]
                dp.pop()
            elif ops[i] == 'D':
                dp.append(2 * int(dp[-1]))
                ans += dp[-1]
            else:
                dp.append(int(ops[i]))
                ans += dp[-1]
        return ans
                
        

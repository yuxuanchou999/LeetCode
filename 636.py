class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stk, prev, res = [], 0, [0] * n
        for i in range(len(logs)):
            if logs[i].split(':')[1] == 'start':
                if stk:
                    res[stk[-1]] += int(logs[i].split(':')[2]) - prev
                stk.append(int(logs[i].split(':')[0]))
                prev = int(logs[i].split(':')[2])
            else:
                res[stk.pop()] += int(logs[i].split(':')[2]) - prev + 1
                prev = int(logs[i].split(':')[2]) + 1
            
            
        return res
                                    
                
                
                                          

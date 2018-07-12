class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        h, m = collections.defaultdict(list), collections.defaultdict(list)
        for i in range(12):
            h[bin(i)[2:].count('1')].append(str(i))
        
        for i in range(60):
            m[bin(i)[2:].count('1')].append(str(i))
            
        for i in range(num + 1):
            for x in h[i]:
                for y in m[num - i]:
                    if len(y) < 2:
                        res.append(x + ':0' + y)
                    else:
                        res.append(x + ':' + y)
        return res
                    
            
            

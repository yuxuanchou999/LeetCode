class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res, self.target = [], target
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)
        return res
    
    def dfs(self, num, temp, cur, last, res):
        if not num and self.target == cur:
            res.append(temp)
            return
        
        for i in range(1, len(num) + 1):
            val = int(num[:i])
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], temp + '+' + num[:i], cur + val, val, res)
                self.dfs(num[i:], temp + '-' + num[:i], cur - val, -val, res)
                self.dfs(num[i:], temp + '*' + num[:i], cur - last + last * val, last * val, res)


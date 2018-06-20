class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        dic = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/': operator.floordiv}
        op1, op2, x = [], [], 0
        while x < len(s):
            if s[x] == ' ': 
                x += 1
                continue
            elif s[x].isdigit():
                new = ''
                while x < len(s) and s[x].isdigit():
                    new += s[x]
                    x += 1
                if not op2 or op2[-1] in '-+':
                    op1.append(int(new))
                else:
                    op1.append(dic[op2.pop()](op1.pop(), int(new)))
            else:
                op2.append(s[x])
                x += 1
                
        val = op1.pop(0)
        while op1:
            val = dic[op2.pop(0)](val, op1.pop(0))
            
        return val
                
                
                

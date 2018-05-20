class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'+':operator.add, '-':operator.sub}
        i, op, num = 0, [], []
        while i < len(s):
            if s[i] == ' ': 
                i += 1
                continue
            elif s[i] == '(' or s[i] == '+' or s[i] == '-':
                op.append(s[i])
                i += 1
            elif s[i] == ')':
                op.pop()
                if len(op) == 0: 
                    i += 1
                    continue
                num[-2] = dic[op.pop()](num[-2], num[-1])
                num.pop()
                i += 1
            elif '0' <= s[i] <= '9':
                new = ''
                while i < len(s) and '0' <= s[i] <= '9':
                    new += s[i]
                    i += 1
                if len(op) > 0 and op[-1] in dic:
                    num[-1] = dic[op.pop()](num[-1], int(new))
                else:
                    num.append(int(new))
        return num[-1]

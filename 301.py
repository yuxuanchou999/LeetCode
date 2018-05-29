class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        def isValid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0: return False
            
            return cnt == 0
        
        level = {s}
        while True:
            valid = filter(isValid, level)
            if valid: return valid
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}

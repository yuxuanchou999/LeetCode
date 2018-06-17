class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack, token = [], path.split('/')
        for t in token:
            if t == '..' and stack:
                stack.pop()
            elif t != '..' and t != '.' and t:
                stack.append(t)
                
        return '/' + '/'.join(stack)

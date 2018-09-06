class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def build(x):
            ans = []
            for i in x:
                if i == '#' and ans:
                    ans.pop()
                elif i != '#':
                    ans.append(i)
            return ans
        
        return build(S) == build(T)

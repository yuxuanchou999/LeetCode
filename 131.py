class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def helper(s, i, cur):
            if i == len(s):
                res.append(list(cur))
            else:
                for j in range(i, len(s)):
                    if s[i:j + 1] == s[i:j + 1][::-1]:
                        cur.append(s[i:j + 1])
                        helper(s, j + 1, cur)
                        cur.pop()
        
        res = []
        helper(s, 0, [])
        return res
        
    
    
            
        

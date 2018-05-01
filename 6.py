class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = len(s)
        if numRows < 2 or l <= numRows:
            return s
        else:
            n = (l - numRows)//(2*(numRows - 1)) + 1
        a = []
        for i in range(numRows):
            a += s[i]
            j = 0
            while j < n:
                if i == 0 or i == numRows - 1:
                    if i+2*(numRows-1)*(j+1) < l:
                        a += s[i+2*(numRows-1)*(j+1)]
                    else:
                        break
                else:
                    if 2*(numRows-1)*(j+1)-i < l:
                        a += s[2*(numRows-1)*(j+1)-i]
                    else:
                        break
                    if 2*(numRows-1)*(j+1)+i < l:
                        a += s[2*(numRows-1)*(j+1)+i]
                    else:
                        break
                j += 1
        return ''.join(a)
            
                

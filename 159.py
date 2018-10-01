class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        if len(set(s)) <= 2: return len(s)
        l, r, length, curr = 0, 1, 1, {s[0]:0}
        while r < len(s):
            if s[r] not in curr:
                if len(curr) == 2:
                    length = max(length, r - l)
                    l = min(curr[x] for x in curr) + 1
                    curr = {s[r - 1]:r - 1, s[r]:r}
                else:
                    curr[s[r]] = r
            else:
                curr[s[r]] = r
            r += 1
                
        return max(length, r - l)
        
        
        
